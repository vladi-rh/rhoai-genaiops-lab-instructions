## Deploy Canopy Test & Prod

We deployed our `canopy` in experiment environment manually, but for the higher environments we need to store the definitions in Git and deploy our models via Argo CD to get all the benefits that GitOps brings.


1. Just like we did with our toolings, we need to generate `ApplicationSet` definition for our model deployment. We will have two separated `ApplicationSet` definition; one is for `test` and one is for `prod` environment. For the enablement simplicity reasons, we keep them in the same repository. However in the real life, you may also like to take prod definitions into another repository where you only make changes via Pull Requests with a protected `main` branch. We keep `ApplicationSet` definition separate so that it'll be easy to take the prod definition into another place later on :)

    Let's update the `ApplicationSet` definition with `CLUSTER_DOMAIN` and `USER_NAME` definition just like before. Open up the `genaiops-gitops/appset-test.yaml` and `genaiops-gitops/appset-prod.yaml` files and replace the values. For the lazy ones we also have the commands:

  ```bash
    sed -i -e 's/CLUSTER_DOMAIN/<CLUSTER_DOMAIN>/g' /opt/app-root/src/genaiops-gitops/appset-test.yaml
    sed -i -e 's/USER_NAME/<USER_NAME>/g' /opt/app-root/src/genaiops-gitops/appset-test.yaml
    sed -i -e 's/CLUSTER_DOMAIN/<CLUSTER_DOMAIN>/g' /opt/app-root/src/genaiops-gitops/appset-prod.yaml
    sed -i -e 's/USER_NAME/<USER_NAME>/g' /opt/app-root/src/genaiops-gitops/appset-prod.yaml
  ```

1. Let's add `canopy-ui` definition. We created two files since we have two different environments; `test` and `prod`. So we have two files to update. Update both `canopy/test/canopy-ui/config.yaml` and `canopy/prod/canopy-ui/config.yaml` files as follow. 

    This will take UI deployment helm-chart and apply the additional configuration such as image version.  

    ```yaml
    repo_url: https://<GIT_SERVER>/<USER_NAME>/canopy-ui
    chart_path: chart
    name: canopy
    BACKEND_ENDPOINT: "http://canopy-backend:8000"
    image:
    name: "canopy-ui"
    tag: "0.2"
    ```
2. Let's get this deployed of course - it's not real unless its in git!

    ```bash
    cd /opt/app-root/src/genaiops-gitops
    git add .
    git commit -m  "🌳 ADD - ApplicationSets and Canopy UI to deploy 🌳"
    git push 
    ```

3. With the `canopy-ui` values stored in Git, now let's tell Argo CD to start picking up changes to these environments. To do this, simply we need to create ApplicationSets:

    ```bash
    oc apply -f /opt/app-root/src/genaiops-gitops/appset-test.yaml -n <USER_NAME>-toolings
    oc apply -f /opt/app-root/src/genaiops-gitops/appset-prod.yaml -n <USER_NAME>-toolings
    ```

4. You should see the two canopy application, one for `test` and one for `prod` deployed in Argo CD. 

    

5. You can also go to OpenShift Console, check `<USER_NAME>-test` namespace to see if the app is deployed.






## Git Monitor Dashboard

Now let's add a Git Monitor dashboard to track changes to our model and prompt configurations in real-time. This dashboard will show you exactly what changes are being made to your `values-test.yaml` and `values-prod.yaml` files.

### Setting up the Git Monitor

The Git Monitor is a web application that tracks changes to your model and prompt configurations directly from your Git repository. It displays:

- **Environment** (Test vs Production)
- **Use Case** (what the model is used for)
- **Model** (which model is being used)
- **Prompt** (the actual prompt text)
- **Status** (enabled/disabled)
- **Commit Information** (when and who made the change)

### Embedded Git Monitor Dashboard

Below is the live Git Monitor dashboard that will automatically update when you make changes to your repository:

<iframe 
  src="http://localhost:5001/?git_repo_url=https://<GIT_SERVER>/<USER_NAME>/canopy-be.git&git_username=<USER_NAME>&git_password=<PASSWORD>&git_branch=main&monitor_interval=30" 
  width="100%" 
  height="600px" 
  frameborder="0" 
  style="border: 1px solid #ccc; border-radius: 8px;">
</iframe>

> **Note:** Replace `<GIT_SERVER>`, `<USER_NAME>`, and `<PASSWORD>` with your actual values. The dashboard will automatically refresh every 30 seconds to show the latest changes.

### How to Use the Dashboard

1. **Real-time Updates**: The dashboard automatically checks for new commits every 30 seconds
2. **Manual Refresh**: Click the "🔄 Refresh" button to manually update the data
3. **Hover for Details**: Hover over long prompts to see the full text
4. **Track Changes**: See exactly when models or prompts were changed and by whom

### Testing the Git Monitor

To test the Git Monitor, try making a change to your model configuration:

1. Edit your `chart/values-test.yaml` file in the `genaiops-gitops` repository
2. Change the model or prompt text
3. Commit and push the changes
4. Watch the dashboard update with your new changes

Example change:
```yaml
# chart/values-test.yaml
LLAMA_STACK_URL: "http://llama-stack"
summarize:
  enabled: true
  model: llama32  
  prompt: | # Try changing the prompt
    Please provide a comprehensive summary of the following text.  
```

The dashboard will automatically detect this change and display it in the table with the commit information and author details. 