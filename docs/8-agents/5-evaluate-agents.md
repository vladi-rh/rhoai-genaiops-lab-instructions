# Evaluate Agents [WIP]

Your agent is now live, helping students and scheduling meetings with professors. But here's the thing - how do you know it's actually working correctly?

Just like with testing in the earlier chapters, the same question gets answered differently every time. And that's fine... usually, but makes things a bit tricky.

## Three layers of agent testing

When evaluating agents, we will focus on three areas:

1. **Unit tests for individual tools** - Test each tool in isolation. Does the calendar API actually create events? Does the search return relevant results?
2. **Text-to-JSON validation** - Can the LLM format tool calls correctly, and does it choose the right tools? (Spoiler: malformed JSON is where most agents break)
3. **End-to-end evaluation** - Does the complete workflow help users?

We've already set up an eval framework earlier, so let's put it to work testing our agent!


