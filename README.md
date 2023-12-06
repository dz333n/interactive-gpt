# Interactive GPT

The simple way for ChatGPT to execute your prompts on your device.

## Prompt examples

- `Open YouTube`
- `Open Windows explorer`
- `Open My Documents`
- `Set Windows volume to 50%`

## How it works?

This program is an interactive Python script that integrates with OpenAI's GPT models. It takes user inputs, processes them using GPT, and attempts to execute the resulting Python code. The program includes functions to dynamically install missing Python modules, handle execution errors, and color-code console outputs for better readability.

Key aspects:

- **Integration with OpenAI GPT Models:** Uses the OpenAI API to generate Python code based on user inputs.
- **Dynamic Execution of Python Code:** Executes the Python code generated by the GPT model.
- **Handling of Missing Modules:** Automatically installs any missing Python modules required for the execution of the generated code.
- **Error Handling:** Captures and handles exceptions during code execution.
- **Security Concerns:** It's important to note that executing code generated in this manner can be unsafe, as it may execute arbitrary and potentially harmful code.

⚠️ This script is a powerful tool but should be used with caution due to the risks associated with executing dynamically generated code.

Interesting fact: this script and document were written by ChatGPT as part of the program to replace people with artificial intelligence.