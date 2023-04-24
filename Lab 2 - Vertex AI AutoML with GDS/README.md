# Lab 2 - Vertex AI AutoML with GDS

## Vertex AI Workbench
Now that we've done some very light weight exploration, let's try using a more full featured environment, Vertex AI Workbench.  Open up the [Google Cloud Console](https://console.cloud.google.com/).

Type Vertex AI in the search bar.

![](images/01-console.png)

Click on the first result.

![](images/02-search.png)

Dismiss the tutorials dialog.  Click "ENABLE ALL RECOMENDED API."

![](images/03-vertex.png)

That will take a few minutes to run.  You can click on the alert icon in the upper right to view progress.

When complete, click on the Workbench link on the left hand side.

![](images/04-vertex.png)

Workbench is a hosted notebook environment.  Unlike Colab, it's tightly intergrated into Vertex AI.  That means auth is easier and more libraries are installed by default.  Notebooks also keep running if you close you web browser, which is really helpful for long running jobs like AutoML training.  Of course, you need to pay for these hosted environments, whereas a base Colab environment is free.

Since we're testing out all the most advanced Google features, we want to use the fully managed notebooks, note the user managed ones.  Click on "Managed Notebook."

![](images/05-workbench.png)

Click "CREATE NOTEBOOK."

![](images/06-managed.png)

Make a note of the region your notebook is in.  You'll want to create a bucket in that same region later.  Vertex requires locality for the buckets it uses to load and write data.

Keep the defaults and select "CREATE."

![](images/07-create.png)

The notebook creation will take a few minutes to run.  When complete, click "OPEN JUPYTERLAB" to open the Workbench environment.

![](images/08-workbench.png)

You're now presented with a menu of runtimes available.  We're going to clone the notebooks we need for the remainder of this workshop.  We could do this graphically, but let's use the terminal.  Click on the terminal icon.

![](images/09-managed.png)

In the terminal type the command:

    git clone https://github.com/neo4j-partners/mini-hands-on-lab-neo4j-and-vertex-ai.git

![](images/10-terminal.png)

When complete, you should see a message in the terminal as well as a new directory in the file explorer on the left.

![](images/11-clone.png)
 

Let's start by firing up a notebook.  Click on the new "mini-hands-on-lab-neo4j-and-vertex-ai" in the file explorer.  Drill down to Lab 2 and open the [p1-graph-loading.ipynb](p1-graph-loading.ipynb) notebook.  Start up a Python kernel and work through that noteboook!

Once you are done with this notebook, proceed to [p2-graph-feature-eng.ipynb](p2-graph-feature-eng.ipynb) and [p3-vertexai-automl.ipynb](p3-vertexai-automl.ipynb)

![](images/12-kernel.png)

Congratulations on running your notebook in Vertex AI Workbench!