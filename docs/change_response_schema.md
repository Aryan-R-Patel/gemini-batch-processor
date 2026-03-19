# Changing the Response Schema
The application currently uses a simple `TestEntry` response schema for structuring the output from the Gemini model. This schema can be customized to fit different requirements by modifying the Pydantic models and updating the relevant scripts.

## Steps to Change the Response Schema
1. **Define a New Pydantic Model**: Add a new Pydantic model in [models.py](../models.py) that represents your desired response schema. Ensure it inherits from `BaseModel` and defines the necessary fields with appropriate types.
2. **Update the Input Generation Script**: Modify [create_input_jsonl.py](../create_input_jsonl.py) to use the new response schema:
   - Update the import statement to include your new model.
   - Replace the reference to `TestEntry` in the `generation_config` with your new model.
