Requirements
------------
App engine SDK - http://developers.google.com/appengine/downloads

GitHub branching practice.
--------------------------
For each new changelist
git checkout -b <branch>
git fetch
git add ...
git commit ..
git push origin <branch>

Local Testing 
-------------
This runs gae locally
$ python run.py -c -s

Deploying to your app engine account.
------------------------------------
1.change app.yaml in main/ to your app id.
2.$ appcfg.py update main

Unit Testing 
------------
python testrunner.py /usr/local/bin/ $PWD/main/logic/tests
where 
/usr/local/bin points to app engine SDK installation 
and
$PWD/main/logic/tests points to test directory
 
Debugging
---------
localhost:8081/console 
shows an interactive debugger.

