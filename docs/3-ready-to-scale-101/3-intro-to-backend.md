# Canopy Backend

1. We'll deploy the backend to our development environment the same way we deployed the other components. Go back to OpenShift Console, click `+Add` and select `Helm Charts`. Under `Canopy Helm Charts`. Select `Canopy Backend` > `Create`.

    ![canopy-be-helm.png](./images/canopy-be-helm.png)

2. As we discussed, backend will be the one talking to Llama Stack, therefore we need to provide its connection details:

    - LLAMA_STACK_URL: `http://llama-stack`
    - MODEL_NAME: `llama32`
 
    ..leave the rest default and hit `Create`.

3. Verify that it is running on the OpenShift Console.
   
   ![canopy-be-ocp.png](./images/canopy-be-ocp.png)


## Update Canopy Frontend

1. Now it is time to make Canopy UI to talk with backend, instead of directly sending requests to LLM. In order to do that, we need to update some values in our helm chart. In the `Topology` view, find `canopy-ui` and click the three dots underneath > `Upgrade`

    ![update-canopy-ui.png](./images/update-canopy-ui.png)

3. In the values, add below value as `BACKEND_ENDPOINT`.
   
    ```bash
    http://canopy-backend:8000
    ```

    ![update-canopy-ui-2.png](./images/update-canopy-ui-2.png)


4. For the image, point to a newer version:
   
   - tag: `0.2`
  
  ..and hit `Create`!

    ![update-canopy-ui-3.png](./images/update-canopy-ui-3.png)

5. Verify that Canopy UI still works as expected by clicking the little arrow and accesing the UI:
   
    ![update-canopy-ui-4.png](./images/update-canopy-ui-4.png)

6. Ask it to summarize a text again!
   
   ![canopy-ui-llamastack.png](./images/canopy-ui-llamastack.png)

Now that we're happy with the first iteration of our Canopy assistant, it’s time to put it in the hands of real users. To do that, we need to deploy everything we've built so far into a test—and eventually a production—environment. But this time, we’ll do it in a more robust, consistent, and repeatable way. That’s why we’re stepping into the world of: GitOps.