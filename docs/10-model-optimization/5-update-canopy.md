# 🔄 Update Canopy to Use Compressed Llama 3.2 FP8 Model

Let's take our experiment environment from Tiny Llama and point it to the FP8 one. We'll go through the same steps.

## 🦙 Update Llama Stack Configuration

1. Navigate to **OpenShift Console** → **Helm** → **Releases** and find your `llama-stack-operator-instance` release in the `<USER_NAME>-canopy` project.

2. Click on the release and select **Upgrade**.

    ![tiny-llama-upgrade.png](./images/tiny-llama-upgrade.png)

3. Update the model configuration to point to your on-prem endpoint:

    - **Model Name**: `RedHatAI/Llama-3.2-3B-Instruct-FP8`
    - **Model URL**: `http://llama-32-fp8-predictor.ai501.svc.cluster.local:8080/v1`

4. Click **Upgrade** to apply the changes.

    ![tiny-llama-upgrade2.png](./images/tiny-llama-upgrade2.png)

5. Also we need to update the `backend` and we can increase the `max_token` again 😌 Find `canopy-backend` under **OpenShift Console** → **Helm** → **Releases** 

    ![tiny-backend-upgrade.png](./images/tiny-backend-upgrade.png)

6.  Let's first evaluate the summarization use case with the new model. Add these under `summarize`.

    ```yaml
    summarize:
      enabled: true
      max_tokens: 2048 # 👈 update this ❗️❗️❗️
      model: RedHatAI/Llama-3.2-3B-Instruct-FP8 # 👈 update this ❗️❗️❗️
      prompt: "<your prompt>"
    ```

7. Click **Upgrade** to apply the changes.

    ![tiny-backend-upgrade2.png](./images/tiny-backend-upgrade2.png)

### 🌳 Test Canopy with the New Model

Once Llama Stack and backend are back up, let's verify it can communicate with the on-prem model.

1. Go to [Canopy UI](https://canopy-ui-<USER_NAME>-canopy.<CLUSTER_DOMAIN>) and test summarization. You can copy the text about Turkish tea from the previous chapters if you wish ☕️

2. You should receive a response from the quantized model, and still feel like you are using the unquantized one 😌

### Move Test and Prod to On Prem 🦙

WIP - update GitOps, run evals, check results, compare results, check dashboards