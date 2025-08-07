# 📊 Vector Stores: The Foundation of RAG

<div class="terminal-curl"></div>

Think of vector stores as the specialized libraries that power RAG systems. While a traditional library organizes books alphabetically, vector stores organize information by *meaning* - allowing AI to find relevant content based on semantic similarity rather than just keyword matching.

For Canopy at RDU, this means students can ask "How does bias affect hiring?" and get relevant information even if your course materials use terms like "discrimination in recruitment" or "algorithmic fairness in employment."

## 🔍 What are Vector Stores?

![LLS RAG Architecture Diagram](images/rag5.png)

**Vector stores** (also called vector databases) are specialized databases that store and search through high-dimensional vectors - mathematical representations of text meaning. Here's how they work:

### The Vector Magic ✨

1. **Text → Numbers**: Every piece of text gets converted into a list of numbers (a vector) that captures its meaning
2. **Similarity Search**: When you ask a question, the system finds vectors with similar "shapes" in the mathematical space
3. **Lightning Fast**: Even with millions of documents, searches happen in milliseconds

![LLS RAG Architecture Diagram](images/rag6.png)


### Why Regular Databases Aren't Enough

Let's use a simple example to understand the difference. Imagine you're building a pet care app with these documents:

**❌ Traditional Keyword Search:**
- Searching for "dog" only finds documents containing the exact word "dog"
- Misses related documents about "puppy", "canine", "golden retriever", or "border collie"
- A search for "cat care" won't find a document titled "Feline Health Tips"
- Can't understand that "My furry friend loves to fetch" is about dogs

**✅ Vector-Based Semantic Search:**
- Searching for "dog" finds documents about puppies, specific breeds, and dog-related concepts
- Understands that "feline" and "cat" are related, so "cat care" finds "Feline Health Tips"
- Recognizes that "furry friend that fetches" is semantically similar to "dog behavior"
- Ranks results by conceptual relevance: "golden retriever training" scores higher than "cat toys" for a "dog" search

The magic happens because vectors capture *meaning* - "puppy", "canine", and "golden retriever" all get similar vector representations because they're conceptually related, even though they share no common letters!

## 🛠️ Vector Store Options

There are several vector database options available for RAG systems:

- **Milvus**: Open-source, highly scalable, great for production workloads
- **Chroma**: Lightweight, developer-friendly, good for prototyping
- **Pinecone**: Cloud-native, managed service, pay-as-you-scale
- **Weaviate**: GraphQL API, hybrid search capabilities
- **Qdrant**: Written in Rust, high performance, good for large datasets

For this module, we'll use **Milvus** as our vector database - it's open-source, highly scalable, and perfect for educational RAG systems that need to handle multiple courses and thousands of documents.

## 📊 Deploy Milvus Test & Prod

We deployed our vector database concepts in the experimentation phase, but just like with Canopy, we need to set up our vector database deployment to handle test and production environments with proper separation and configuration management.

### 1. Set Up Milvus Directory Structure

We'll create separate configurations for test and prod environments under the canopy directory structure so the existing ApplicationSets can detect them:

```bash
mkdir -p /opt/app-root/src/genaiops-gitops/canopy/test/milvus
mkdir -p /opt/app-root/src/genaiops-gitops/canopy/prod/milvus
touch /opt/app-root/src/genaiops-gitops/canopy/test/milvus/config.yaml
touch /opt/app-root/src/genaiops-gitops/canopy/prod/milvus/config.yaml
```

### 2. Configure Milvus Config Files

`milvus` will use the same configuration for both test and prod environments, keeping it simple. Update both `canopy/test/milvus/config.yaml` and `canopy/prod/milvus/config.yaml` with the same configuration:

**Both TEST and PROD:**

```yaml
chart_path: charts/milvus
```

For now, we're happy with the default Milvus values. We will get some exciting updates as we continue to the other chapters :)

### 3. Deploy via GitOps

Now let's get these configurations deployed! Store all vector database definitions in Git:

```bash
cd /opt/app-root/src/genaiops-gitops
git add .
git commit -m "📊 ADD - Milvus test & prod vector databases 📊"
git push
```

### 4. Deploy with ApplicationSets

With all the vector database configurations stored in Git, the ApplicationSets you created in the previous Canopy deployment chapter will automatically detect the new Milvus configurations and deploy them to the appropriate namespaces:

- **Test Milvus** → deployed to `<USER_NAME>-test` namespace  
- **Prod Milvus** → deployed to `<USER_NAME>-prod` namespace

If you haven't created the ApplicationSets yet, you'll need to update them with your cluster details and apply them:

```bash
# Update ApplicationSet definitions with your cluster domain and username
sed -i -e 's/CLUSTER_DOMAIN/<CLUSTER_DOMAIN>/g' /opt/app-root/src/genaiops-gitops/appset-test.yaml
sed -i -e 's/USER_NAME/<USER_NAME>/g' /opt/app-root/src/genaiops-gitops/appset-test.yaml
sed -i -e 's/CLUSTER_DOMAIN/<CLUSTER_DOMAIN>/g' /opt/app-root/src/genaiops-gitops/appset-prod.yaml
sed -i -e 's/USER_NAME/<USER_NAME>/g' /opt/app-root/src/genaiops-gitops/appset-prod.yaml
```

If you didn't applied yet, apply the new 

```bash
# Apply the ApplicationSets
oc apply -f /opt/app-root/src/genaiops-gitops/appset-test.yaml -n <USER_NAME>-toolings
oc apply -f /opt/app-root/src/genaiops-gitops/appset-prod.yaml -n <USER_NAME>-toolings
```

You can verify the ApplicationSets are running and picking up the new configurations:

```bash
# Verify the ApplicationSets are running
oc get applicationsets -n <USER_NAME>-toolings

# Watch Argo CD automatically create the new Milvus applications
oc get applications -n <USER_NAME>-toolings | grep milvus
```

You should see the two Milvus applications, one for `test` and one for `prod` being automatically deployed by Argo CD to their respective namespaces.

> **💡 Deployment Note**: We're using **standalone deployments** of Milvus with default configurations, which are perfect for development and educational environments. Both test and prod environments provide the full vector database functionality needed for your RAG systems while keeping resource usage reasonable for learning purposes.

### 5. Verify Milvus Deployments

Once deployed, verify both environments are running correctly:

```bash
# Check if Milvus pods are running in test environment
oc get pods -n <USER_NAME>-test | grep milvus

# Check if Milvus pods are running in prod environment  
oc get pods -n <USER_NAME>-prod | grep milvus

# Check the services are accessible
oc get svc -n <USER_NAME>-test | grep milvus
oc get svc -n <USER_NAME>-prod | grep milvus

# View logs if needed for either environment
oc logs -l app=milvus -n <USER_NAME>-test --tail=50
oc logs -l app=milvus -n <USER_NAME>-prod --tail=50
```

You should see output showing Milvus pods in `Running` state in both test and prod namespaces.

## 🎯 Next Steps: Building Intelligent Apps with RAG

With your vector store ready, you now have the foundation for RAG. Next, you'll build the intelligent layer that knows how to search your vector database and create helpful responses for students.

Continue to **[🦙 LlamaStack & RAG](3-llamastack-rag.md)** to connect your vector store with LlamaStack and create your first RAG-powered educational assistant.