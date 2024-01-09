# Infolog

## 1/8/24

NOTES:

- It seems like if I use the pythong API I need to get some sort of cloud account and have a cloud project. I think I have that, but I would rather just use an API key.
    - The rest api allows just sending the API key.
- If you do a multi-turn session (chat), it appears you can only have "user" and "model"
as roles (not including function messages) and that you have to alternate the role, starting
with "user".
    - The attached code shows examples, including function calls and responses.
    - To do a system message, you can do a user message followed by a dummy model message. I 
    also do that in the attached code.