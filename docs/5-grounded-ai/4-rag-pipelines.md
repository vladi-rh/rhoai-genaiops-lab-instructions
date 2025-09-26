# 🌳 Automating RAG with KFP Pipelines

Your document intelligence RAG system works brilliantly in notebooks, but what happens when you need to process hundreds of research papers for your educational platform? 
Manual execution doesn't scale, and RDU needs reliable, always-available intelligent document processing.

## 🔍 Introducing (Again) KFP Pipelines

Now we'll use **Kubeflow Pipelines (KFP)** to transform your experimental RAG system into a production-grade platform that can handle complex academic documents automatically and at scale.

## 🏗️ Document Intelligence RAG Pipeline Architecture

Here is the current architecture we are working with and want to automate.  
We are specifically looking to automate the top part, how new documents go into our vector database.

![Pipeline Architecture](images/rag4.png)

## 🎯 Running Your Production Pipeline

Time to deploy your document intelligence RAG system in production!

1. First, set up persistent storage for content transfer between pipeline stages. One stage might download the documents, the next stage might transform them, and later stage might process them further. Persistent storage ensures each stage can access the outputs of the previous one.

   ```bash
   oc apply -f canopy/5-rag/4-kfp-pipeline-pvc.yaml -n <USER_NAME>-prod
   ```

   This creates a `canopy-workspace-pvc` that allows pipeline components to share processed document content efficiently.

2. Open `canopy/5-rag/6-kfp_pipeline.py`, this is your document processing pipeline. It will:
   - Set up Docling
   - Process the documents
   - Connect to your vector database
   - Add the processed documents to the database
   - And finally, run a test to make sure everything worked well


   Much of this processed is based on these settings/arguments you can find close to the bottom of the pipeline code, review them quick to see that we are doing the same thing as before, now just automated:

   ```python
   arguments = {
       "document_url": "https://arxiv.org/pdf/2404.14661",        # Research paper URL
       "test_queries": [
           "What is the PRFXception mentioned in the document?",   # Academic concept query
       ],
       "embedding_model": "all-MiniLM-L6-v2",                     # Optimized for education
       "embedding_dimension": 384,                                 # Performance-balanced
       "chunk_size_tokens": 512,                                   # Academic content chunks
       "vector_provider": "milvus",                                # Production vector DB
       "docling_service": "http://docling-v0-7-0-predictor.ai501.svc.cluster.local:5001",
       "processing_timeout": 180,                                  # 3 min for complex docs
       "llama_stack_url": "http://llama-stack-service:8321",      # AI inference service
       "model_id": "llama32",                                      # Educational LLM
       "temperature": 0.0,                                         # Deterministic responses
       "max_tokens": 4096                                          # Comprehensive answers
   }
   ```

3. Run your document processing pipeline by running on `python canopy/5-rag/6-kfp_pipeline.py` in your terminal. This should take about 5-6 minutes to complete.

4. We can monitor the progress of our pipeline in OpenShift AI:

   Go to **OpenShift AI Dashboard** → **Experiments** → **Experiments and runs**

   ![Pipeline Monitoring](images/rag9.png)

   You'll see your `document-intelligence-rag` experiment with detailed execution tracking.

5. Click on one of the steps to access information about inputs, outputs, and logs:

   ![Pipeline Monitoring](images/rag10.png)

### What You've Built

🎉 **Congratulations!** You now have a production-ready document processing pipeline that we can use to ingest documents into our test and producion databases at scale.

Continue to **[🌳 Integrating RAG within Canopy](5-rag-Canopy.md)** to enable our RAG feature inside our application! 🚀 