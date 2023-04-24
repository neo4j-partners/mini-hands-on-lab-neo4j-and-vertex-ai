# Discussion - Questions and Next Steps
This section has some thoughts on future work, improvements and next steps.  Please feel free to [PR](https://github.com/neo4j-partners/hands-on-lab-neo4j-and-vertex-ai/pulls) your ideas and suggestions.

## Lab 1 - Deploy Neo4j
The lab deploys Neo4j AuraDS Professional through a deep integration in the Google Cloud Console [here](https://console.cloud.google.com/marketplace/product/endpoints/prod.n4gcp.neo4j.io).  There are many other ways to deploy Neo4j.  If AuraDS Professional doesn't meet your needs, we probably have a different approach that does.  The [Marketplace](https://console.cloud.google.com/marketplace/browse?q=neo4j) is a good place to look for more options.

## Lab 2 - Lab 2 - Vertex AI AutoML with GDS
**Moving Data**

We used LOAD CSV to pull data in.  That is one of many ways.  Neo4j [Data Loader](https://data-importer.neo4j.io/) is another.  We're exploring incorporating it into this lab.

The Neo4j [Spark Connector](https://neo4j.com/docs/spark/current/) is another way to get data in.  We've been working with the Google [Dataproc](https://cloud.google.com/dataproc) team on some demos of that.  It works today but some walkthrough are in progress.

**Graph Data Science**

With a novel data set combined with a novel approach to machine learning, there's enough material here for numerous business applications or academic papers.  Some areas that might be interesting to explore in the future follow.

Some work on tuning the embedding would improve accuracy.

**Vertex AI AutoML**

Vertex AI is an amazing suite of products.  It's largely serverless.  The GUI is intuitive.  It takes almost all the infrastructure pain out of machine learning.  At the same time, it is very very new.  The console is constantly changing.  New features are often introduced with only a REST API.  The APIs change.

AutoML takes ~2 hours to run even with a 1 hour budget.  The nice part about using a SaaS like Vertex AI is that all this is going to improve without any need to manage upgrades, infrastructure, etc.

New features for batch prediction and forecasting were recently released.  We're exploring including those in future versions of this lab as they mature.

## Next Steps
We hope you enjoyed these labs.  If you have any questions, feel free to reach out directly to any of us.  We'd love the opportunity to explore and support your use cases.
