# 🔍 Enable Monitoring

In the context of production GenAI systems, observability is your ability to understand what's happening inside your AI applications by examining the data it produces. Think of it like a teacher monitoring a classroom: you need to see if students are engaged, struggling, or succeeding.

Without observability, running AI in production is like flying blind, you only know something's wrong when users complain. With proper observability, you can spot problems before they impact students and fix issues quickly.

## The Three Pillars of Observability

Modern observability relies on three complementary data types:

* **Metrics** 📊 - Quantitative measurements over time (response latency, request rate, error percentage, time for first token).
* **Logs** 📝 - Detailed event records from your application (error messages, user requests, system events).
* **Traces** 🔍 - Request paths through distributed services (how a student's question flows through Canopy's microservices, MCP tools, and LLMs).

Together, these three pillars give you complete visibility into Canopy's behavior. Let's see how to enable observability for Canopy!

## Red Hat AI Observability Stack

Red Hat OpenShift AI provides [centralized platform observability](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.0/html/managing_openshift_ai/managing-observability_managing-rhoai): an integrated, out-of-the-box solution for monitoring the health and performance of your OpenShift AI instance and user workloads. 

This pre-configured observability stack includes three core components: **OpenTelemetry Collector (OTC)** for standardized telemetry data ingestion, **Prometheus** for metrics storage and alerting, and **Red Hat build of Tempo** for distributed tracing. 

![Obsv 0](./images/obs0.png)

This architecture provides health metrics and alerts for OpenShift AI platform components while offering integration points for external observability tools like **Grafana**.

> **Note**: The RHOAI Observability stack has already been deployed and configured for this lab environment. If you're interested in learning more about the underlying platform configuration, check the `Managing Observability in RHOAI` section under `Administer OpenShift AI platform access, apps, and operations` [documentation](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed).

## 🔍 OpenTelemetry: The Standard for Observability

Red Hat OpenShift AI uses **OpenTelemetry** (OTel), the open-source standard for distributed tracing and metrics collection. OpenTelemetry provides:

* **Automatic instrumentation** for common frameworks (Flask, FastAPI, Express, etc.)
* **Manual instrumentation** for custom operations specific to your application
* **Vendor-neutral format** that works with any tracing backend
* **Integration with metrics and logs** for complete observability

### OpenTelemetry 🔍 And LlamaStack 🦙

LlamaStack has built-in [OpenTelemetry support](https://llamastack.github.io/docs/building_applications/telemetry#configuration) through its **meta-reference telemetry provider**, which automatically instruments inference operations to generate observability data including traces and metrics. Unlike Canopy's components that use auto-injection, LlamaStack's telemetry is configured directly through environment variables.

**How LlamaStack Telemetry Works:**

When telemetry is enabled, LlamaStack automatically creates spans for each inference request and emits token usage metrics. Each request generates:
- **Traces**: Distributed traces showing the inference request flow with timing data
- **Metrics**: Token counters (`llama_stack_prompt_tokens_total`, `llama_stack_completion_tokens_total`, `llama_stack_tokens_total`) labeled by `model_id` and `provider_id`

The telemetry configuration in the LlamaStack deployment includes:

  <div class="highlight" style="background: #f7f7f7; overflow-x: auto; padding: 8px;">
  <pre><code class="language-yaml"> 
  env:
    - name: OTEL_SERVICE_NAME
      value: llamastack-user1-canopy  # Identifies this instance
    - name: OTEL_EXPORTER_OTLP_ENDPOINT
      value: http://data-science-collector-collector-headless.redhat-ods-monitoring:4318
    - name: TELEMETRY_SINKS
      value: otel_trace, otel_metric  # Enables both traces and metrics
  </code></pre>
  </div>

These environment variables configure LlamaStack to:
1. Export telemetry data to the RHOAI OpenTelemetry Collector via OTLP (port 4318)
2. Enable both trace and metric sinks for comprehensive observability
3. Tag all telemetry with the service name for filtering in Tempo and Prometheus

> **Note**: OpenTelemetry is pre-configured in your [LlamaStack Helm chart](https://github.com/rhoai-genaiops/genaiops-helmcharts/blob/main/charts/llama-stack-operator-instance/templates/lls-distribution.yaml#L15), so metrics and traces are automatically collected without additional setup.

## Deploy Grafana

The RHOAI Observability stack collects platform-wide metrics, but these are generic infrastructure signals that don't reveal application-specific insights about your Canopy deployment. To visualize what matters for your AI assistant - token usage patterns, LLM latency, backend API performance - you need custom Grafana dashboards that query Prometheus with filters specific to your namespace and components.

1. Deploy a Grafana instance in your toolings namespace to support the end-to-end observability journey for Canopy. Install it through your GitOps workflow in `genaiops-gitops/toolings/`:

    Create `grafana` folder under `toolings`. And then create a file called `config.yaml` under `grafana` folder. Or simply run the below commands:

    ```bash
    mkdir /opt/app-root/src/genaiops-gitops/toolings/grafana
    touch /opt/app-root/src/genaiops-gitops/toolings/grafana/config.yaml
    ```

2. Open up the `grafana/config.yaml` file and paste the below line to let Argo CD know which chart we want to deploy.

    ```yaml
    chart_path: charts/grafana
    ```

3. Commit the changes to the repo as you’ve done before.

    ```bash
    cd /opt/app-root/src/genaiops-gitops
    git pull
    git add .
    git commit -m "📈 Grafana added 📈"
    git push
    ```

4. Once this change has been sync’d (you can check this in Argo CD), let’s login to Grafana by clicking [here](https://canopy-grafana-route-<USER_NAME>-toolings.<CLUSTER_DOMAIN>) and view the predefined dashboards for canopy. Alternatively, you can use the run the below command in your code-server workbench terminal:

    ```bash
    # get the route and open it in your browser
    echo https://$(oc get route canopy-grafana-route --template='{{ .spec.host }}' -n <USER_NAME>-toolings)
    ```

    Use your OpenShift credentials and click `Allow selected permissions` to log in.

5. To view the dashboards, navigate to **Dashboards** → **Browse** and look for the `<USER_NAME>-toolings Canopy Dashboards` folder.

   ![Obsv 1](./images/metrics1.png)

## 🎯 Next Steps: Exploring Your AI Stack Metrics

Now everything is deployed and connected to the RHOAI Observability Stack, you're ready to explore the metrics from your AI assistant stack. The dashboards provide real-time visibility into vLLM model performance, Canopy UI/Backend health, and LlamaStack metrics.

Continue to **[Metrics](7-observability/2-metrics.md)** to understand what these dashboards reveal about your application's performance and how to use them for debugging and optimization.