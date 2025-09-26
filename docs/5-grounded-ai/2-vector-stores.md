# 📊 Vector Stores: The Foundation of RAG

<div class="terminal-curl"></div>

We have seen the use of embeddings, and in the last section we used an in-line vector database to store these embeddings.

You can think of vector databases as the specialized libraries that power RAG systems. While a traditional library organizes books alphabetically, vector stores organize information by **meaning**, allowing AI to find relevant content based on semantic similarity (how close the meaning of two sentences are to each other) rather than just keyword matching.  
For example: 
- “The boy kicked the ball into the net.”
- “A child scored a goal by striking the soccer ball.”

Word by word these are very different, but semantically they are almost identical.

## 📊 Deploy Milvus Test & Prod

Using an in-line database of any kind is not something we would want to do in production though, so first thing we want is to deploy a dedicated vector database that we can use to store our embeddings and text.  
For this, we are going to set up Milvus. If you recognize the name it's because it's the same database that we were using in-line just in the previous notebook.

1. Go back to your workbench 🧑‍🏭

2. Set Up Milvus Directory Structure

    We'll create separate configurations for test and prod environments under the canopy directory structure so the existing ApplicationSets can detect them:

    ```bash
    mkdir -p /opt/app-root/src/genaiops-gitops/canopy/test/milvus
    mkdir -p /opt/app-root/src/genaiops-gitops/canopy/prod/milvus
    touch /opt/app-root/src/genaiops-gitops/canopy/test/milvus/config.yaml
    touch /opt/app-root/src/genaiops-gitops/canopy/prod/milvus/config.yaml
    ```

3. Configure Milvus Config Files

    `milvus` will use the same configuration for both test and prod environments, keeping it simple. Update both `canopy/test/milvus/config.yaml` and `canopy/prod/milvus/config.yaml` with the same configuration:

    **Both TEST and PROD:**

    ```yaml
    chart_path: charts/milvus
    ```

    For now, we're happy with the default Milvus values. We will get some exciting updates as we continue to the other chapters 🤭

4. Deploy via GitOps

    Now let's get these configurations deployed! Store all vector database definitions in Git:

    ```bash
    cd /opt/app-root/src/genaiops-gitops
    git add .
    git commit -m "📊 ADD - Milvus test & prod vector databases 📊"
    git push
    ```

    > **💡 Deployment Note**: We're using **standalone deployments** of Milvus with default configurations, which are perfect for test and prod environments. Both provide the full vector database functionality needed for your RAG systems while keeping resource usage reasonable for learning purposes.

5. Each Milvus deployment includes Attu, a powerful web-based administration tool for managing and visualizing your vector database.
    Let's take a look at the test one we just deployed!
    ```
    https://milvus-test-attu-<USER_NAME>-test.<CLUSTER_DOMAIN>
    ```
    We will soon fix that, but first...
    <!-- As you can see, it's completely empty, let's fix that 🔨  
    Go to your workbench and complete the hands-on exercises in `canopy/5-rag/3-vector-databases.ipynb`.  
    This walks you through interacting with the vector database (without Llama Stack, we will add in Llama Stack for test and prod soon). -->

6. Udate your Llama Stack in Test and Prod by opening up `genaiops-gitops/canopy/test/llama-stack/config.yaml` (test) and `genaiops-gitops/canopy/prod/llama-stack/config.yaml` (prod) and update the file as below:

    ```yaml
    ---
    chart_path: charts/llama-stack-operator-instance
    eval:
      enabled: true
    rag:                  # 👈 Add this 
      enabled: true       # 👈 Add this 
    ```
    > **💡 Deployment Note**: This will update our Llama Stack to point to our newly deployed Milvus Vector Database, if you are curious how this looks like you can find the `llama-stack-config` inside ConfigMaps in either your test or dev encironment

7. Let's push the changes for Argo CD to make the necessary changes.

    ```bash
    cd /opt/app-root/src/genaiops-gitops
    git add .
    git commit -m "📚 enable RAG 📚"
    git push origin main
    ```

8. Now that we have our Vector Database set up and connected to our Llama Stack, we can populate it with some data!
    We have two ways to do this:
    - We can either go through Llama Stack (this will look identicall to what we did in `2-intro-to-RAG.ipynb`) or
    - We can connect directly to Milvus.
    
    Let's connect directly to Milvus to see how this looks like.  
    To do that, go to your workbench and complete the hands-on exercises in `canopy/5-rag/3-vector-databases.ipynb` 


## 🎯 Next Steps: Intelligent Data Processing

Next, continue to **[Docling](./3-docling.md)** to learn how to get more complex data into your vector database 🙌