# Take Agents to Prod

Now that we have our new fresh agent, let's take it to production!  
There are a few things we want to do, such as evaluating and observing the agent, but let's start with adding in the feature flag to enable it in the backend.

## Deploy the Agent through GitOps

1. We need to start by upgrading our test and prod Llama Stack, go to `genaiops-gitops/canopy/test/llama-stack/config.yaml` and update to this:

    ```yaml
    chart_path: charts/llama-stack-operator-instance
    eval:
      enabled: true
    rag:                  
      enabled: true
    mcp:                # 👈 Add this 
      enabled: true     # 👈 Add this 
    ```

2. Push this to git so that it takes effect:

    ```bash
    cd /opt/app-root/src/genaiops-gitops
    git add .
    git commit -m "📃 enable MCP 📃"
    git push origin main
    ```

3. After Llama Stack has MCP enabled, we need to update our Canopy backend so it can use the agent feature.  
    Go to your workbench and open the file `backend/chart/values-test.yaml`

4. Edit the file to contain the `student-assistant` feature flag. Feel free to change the prompt, this is the system prompt just like before.

    ```yaml
    LLAMA_STACK_URL: "http://llama-stack-service:8321"
    summarize:
     enabled: true
     model: llama32
     temperature: 0.9
     max_tokens: 4096
     prompt: |
       You are a helpful assistant. Summarize the given text please.
    information-search:
     enabled: true
     vector_db_id: latest
     model: llama32
     prompt: |
       You are a helpful assistant specializing in document intelligence and academic content analysis.
    student-assistant:         # 👈 add this block
     enabled: true
     model: llama32
     temperature: 0.1
     vector_db_id: latest
     mcp_calendar_url: "http://canopy-mcp-calendar-mcp-server:8080/sse"
     prompt: |
    ```

5. Push the change to git:

    ```bash
    cd /opt/app-root/src/backend/chart
    git add values-test.yaml
    git commit -m "🤖 Agent Feature Added 🤖"
    git push
    ```

6. Open the Canopy UI, change to the Student Assistant on the left side and ask `Tell me about quantum entaglement.`.  
    The agent should try to find the information, fail, and then find a professor to help you and schedule a call with them.  
    If you don't have the Canopy open any longer, you can find it here: [https://canopy-ui-<USER_NAME>-test.<CLUSTER_DOMAIN>](https://canopy-ui-<USER_NAME>-test.<CLUSTER_DOMAIN>)

    ![ask-canopy.png](images/ask-canopy.png) [TODO: Screnshot]