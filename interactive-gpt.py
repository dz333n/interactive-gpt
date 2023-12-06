import openai
import subprocess
import sys

rules = """
Rules:
1. If it is possible, no extra info required. Please reply with only the result Python code.
2. If it is impossible or the request does not make sense, then start your response with "Error:"'
"""


def install_module(module_name):
    """
    Install a Python module using pip.
    """
    print_colored(f" ⚠️ Attempting to install missing module: {module_name}", "yellow")
    subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])


def execute_string_as_code(code_string):
    """
    Execute a multi-line string as Python code, handle exceptions, and
    attempt to install missing modules.
    """
    while True:
        try:
            print_colored(code_string, "yellow")
            print_colored("\n 😱😱😱 Executing the code 😱😱😱 \n", "cyan")

            exec(code_string)

            print_colored(" ✅ Executed", "green")
            break  # Break the loop if the code executed successfully
        except ModuleNotFoundError as e:
            missing_module = str(e).split("'")[
                1
            ]  # Extract the module name from the exception message
            print(f"Attempting to install missing module: {missing_module}")
            install_module(missing_module)
        except Exception as e:
            print_colored(f"An error occurred: {e}", "red")
            break  # Exit the loop if an error other than ModuleNotFoundError occurs


def print_colored(text, color):
    """
    Print text in the specified color to the console.
    """
    colors = {
        "standard": "\033[0m",
        "cyan": "\033[96m",
        "yellow": "\033[93m",
        "red": "\033[91m",
        "green": "\033[92m",
    }
    color_code = colors.get(color, colors["standard"])
    print(f"{color_code}{text}{colors['standard']}")


def read_string_from_file(file_name):
    """
    Read a single line from a file and handle file not found exception.
    """
    try:
        with open(file_name, "r") as file:
            return file.readline().strip()
    except FileNotFoundError:
        return "File not found."


def extract_python_code(markdown_string):
    """
    Extract Python code from a markdown string.
    """
    lines = markdown_string.split("\n")
    start_python_code = False
    python_code = []

    for line in lines:
        if line.strip() == "```python":
            start_python_code = True
            continue
        if line.strip() == "```" and start_python_code:
            break
        if start_python_code:
            python_code.append(line)

    return "\n".join(python_code)


def main():
    """
    Main function to run the interactive GPT interface.
    """
    token = read_string_from_file("token")
    if token == "File not found.":
        print_colored("Error: provide your OpenAI token in ./token file", "red")
        sys.exit(1)

    openai.api_key = token
    gpt_model = "gpt-4"

    if len(sys.argv) > 1:
        gpt_model = sys.argv[1]

    print_colored(f"Interactive GPT, running {gpt_model}", "green")

    while True:
        user_input = input(" > Your request: ")
        if user_input.lower() == "exit":
            print_colored("Bye", "cyan")
            break

        process_user_input(user_input, gpt_model)


def process_user_input(user_input, gpt_model):
    """
    Process user input and interact with the GPT model.
    """
    print_colored(" ⌚ Working on your prompt...", "cyan")
    prompt = (
        f'Write a python that would perform the next action: "{user_input}"\n{rules}'
    )

    chat = openai.ChatCompletion.create(
        model=gpt_model, messages=[{"role": "user", "content": prompt}]
    )

    reply = chat.choices[0].message.content

    if reply.startswith("Error:"):
        print_colored(reply, "red")
    else:
        code = extract_python_code(reply)
        execute_string_as_code(code)


if __name__ == "__main__":
    main()
