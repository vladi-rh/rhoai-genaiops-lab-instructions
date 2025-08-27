# Automatically trigger on git changes

Now that we have successfully ran our evaluation pipeline (🎉), we would like it to run automatically everytime we make a change to our tests, prompts, or backend.  
To do this, we can create a Tekton pipeline with a git hook to the relevant repos. This Tekton pipeline will then trigger our evaluation kubeflow pipeline. 🔗

## Trigger kfp through a Tekton pipeline

1. Go to your workbench and clone the repo that contains the Tekton pipeline definition:

    ```bash
    cd /opt/app-root/src
    git clone https://<USER_NAME>:<PASSWORD>@gitea-gitea.<CLUSTER_DOMAIN>/<USER_NAME>/genaiops-helmcharts.git
    ```
    Feel free to look around, the Tekton pipeline definition is inside `charts/pipelines`.


2. Now let's deploy the Tekton pipeline through ArgoCD by running: 

    ```bash
    mkdir /opt/app-root/src/genaiops-gitops/toolings/evaluation-pipeline
    touch /opt/app-root/src/genaiops-gitops/toolings/evaluation-pipeline/config.yaml
    ```
    This will create a yamlfile inside 

2. Open up the ct-pipeline/config.yaml file and paste the below yaml to config.yaml.

    ```bash
    repo_url: https://gitea-gitea.apps.<CLUSTER_DOMAIN>/<USER_NAME>/canopy-evals.git
    chart_path: test_pipeline/canopy-tekton-pipeline
    USER_NAME: user1
    kfp.baseUrl: http://llama-stack.<USER_NAME>-canopy.svc.cluster.local:80
    kfp.backendUrl: http://canopy-backend.<USER_NAME>-canopy.svc.cluster.local:8000
    ```

2. And finally commit it to git, as it only counts if it's in git 😉

    ```bash
    cd /opt/app-root/src/genaiops-gitops
    git add .
    git commit -m "🚄 Evaluation Pipelines 🚄"
    git push
    ```

2. Now let's look at it by going to the OpenShift Dashboard -> Pipelines -> `canopy-test-pipeline`. You can see that all it does is a simple git clone followed by starting the kubeflow pipeline.  

3. Great, we have our pipeline! However, so far we would still need to trigger it manually, the only difference from before is that we now trigger a Tekton pipeline that then triggers our Kubeflow pipeline and nothing more...

    ![super-important-meme](images/super-important-meme.jpg)

    To get some use of our Tekton pipeline, let's make it trigger automatically from our git repos.  
    Start by going to Gitea.
4. Inside of Gitea, navigate to your `canopy-evals` repository.
5. Go to Settings -> Webhooks
6. Click `Add` and choose Gitea
7. Enter `<TODO: Pipeline-trigger-url>` -> click Add
8. Now we can test if this worked by clicking on `Test webhook connection`.  
    You can go to the pipeline view in OpenShift to see if the pipeline started properly.  
9. Now do the same for the `canopy-backend` repo as well.
10. Whenever the pipeline is ran it produces and saves the eval results in your MinIO bucket. You can go there to see how you did: <TODO: minio bucket url>

Congratulations! You have now added testing pipelines to your backend and eval repos, so whenever you update your evaluations or your backend repo, you will run through the tests.

## Try updating your prompt

So far, we have only ran the pipeline with predefined tests, let's go and add some useful tests on our own 🧪

1. Go to your workbench and clone the canopy-evals repo by running this in your terminal:

    ```bash
    git clone 
    ```