From our original architecture:

*The core of Rosie is the application server. This server will be built on the Flask framework and will expose two main interfaces: (1) a JSON API that interacts with the Github API and (2) an HTML frontend that the user can navigate. 

The server's primary responsibility is to handle the post-recieve WebHook from Github. This webhook POSTs data to our server in the following form:*

```json

{
  "before": "5aef35982fb2d34e9d9d4502f6ede1072793222d",
  "repository": {
    "url": "http://github.com/defunkt/github",
    "name": "github",
    "description": "You're lookin' at it.",
    "watchers": 5,
    "forks": 2,
    "private": 1,
    "owner": {
      "email": "chris@ozmm.org",
      "name": "defunkt"
    }
  },
  "commits": [
    {
      "id": "41a212ee83ca127e3c8cf465891ab7216a705f59",
      "url": "http://github.com/defunkt/github/commit/41a212ee83ca127e3c8cf465891ab7216a705f59",
      "author": {
        "email": "chris@ozmm.org",
        "name": "Chris Wanstrath"
      },
      "message": "okay i give in",
      "timestamp": "2008-02-15T14:57:17-08:00",
      "added": ["filepath.rb"]
    },
    {
      "id": "de8251ff97ee194a289832576287d6f8ad74e3d0",
      "url": "http://github.com/defunkt/github/commit/de8251ff97ee194a289832576287d6f8ad74e3d0",
      "author": {
        "email": "chris@ozmm.org",
        "name": "Chris Wanstrath"
      },
      "message": "update pricing a tad",
      "timestamp": "2008-02-15T14:36:34-08:00"
    }
  ],
  "after": "de8251ff97ee194a289832576287d6f8ad74e3d0",
  "ref": "refs/heads/master"
}

```

*The server must parse that JSON, split the commits into seperate builds, store them in the DB and then start a worker thread if one is not already running. All of this should be reasonably simple.*

One piece of additional context for the Application Server is necessary. This component will be deployed on a server (or PAAS like Heroku). No central hosting repository for these servers will be provided by us; rather, each user of Rosie, will need to set up the Application Server on their own server--mostly handling the configuration of that server themselves. However, we hope to make this process extremely easy by enabling the creation of a Git repository (including both our code and the user's code for which they need CI) using a single line CLI command, which can then be deployed to Heroku.

The Application Server is the core of the entire system. It is responsible for:

* exposing API routes that handle JSON data from the Github web hooks and the CLI build command
* exposing an HTML interface to examine blame logs, configure the project, and enqueue new builds
* instantiating Build objects from that JSON data and persisting them in the MongoDB
* instantiating the Queue object
* instantiating and running new WorkerThreads when the Queue has builds enqueued

There are two primary external interfaces for the Application Server:

1. JSON API

The JSON API exposes the following routes:

* '/build'

This route handles Github Webhooks with commit data and CLI build commands. This will enqueue the appropriate Build with the information is parses from the JSON data and start a Worker Thread if one is not already running. It must respond to POST HTTP requests and return a 200OK status code if the build is successfully enqueued, a 400 Bad Request status code if the request is malformed, and a 500 Internal Server Error status code if an error occurs while enqueuing the build.
It must also be followed with requests from the server to GitHub to retrieve the code in each commit so that the Build object will be complete in the database when the worker begins looking for it. Once it has retreived and formatted each commit and stored them in the DB, it returns.

* '/ping'

This route returns JSON data on the current status of the server. If it is building, this would be in the following form:

```json
{
    status: 'building',
    id: 123456,
    remaining: 5
}
```

If it is not building, this reponse would be in the following form:

```json
{
    status: 'success'
}
```

2. HTML Frontend

This HTML front end will expose the following routes:

* '/builds/<build_id>'

This route will show the build status of the build with `id = build_id`. If the build is enqueued, it will simply say 'enqueued'. If it is building, it will say 'building.' If it succeeded, it will say 'success.' If it failed, it will show the stack trace for the failure and the author of the commit that broke the build.

* '/builds'

This route will show a short summary of the build status of all builds.

* '/settings'

This route will expose adjustable settings for the Rosie server.

* '/blame'

This route will expose a ranking of the authors of commits by how many times they have broken a build (yes, we like to shame people).

* '/builds/new'

This route will expose the ability to rebuild any builds that have already been built. This allows users to see if older builds fail new tests.

The Application Server must fulfill the following requirements:

* must expose an API route that accepts JSON to enqueue a new build
* must expose an API route that gives the status of the server
* must expose an HTML route that displays the status of a given build
* must expose an HTML route that displays the status of all builds
* must expose an HTML route that allows the configuration of the Rosie server to be adjusted
* must expose an HTML route that displays the blame rankings for committers
* must expose an HTML route that allows the enqueueing of past builds
* must instantiate a new Queue on start up
* must enqueue any build recieved in the Queue
* must start a WorkerThread if no Worker Thread is running and a build is enqueued
* must instantiate a Build object with the correct data and persist it in MongoDB

