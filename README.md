# wikingrams

This is WikiNGrams.

## Local development

Install npm dependencies:

    cd hseling_web_wikingrams/src/web/static; npm install .; cd ../../../..

## API development

You can develop your API without docker environment:

    cd hseling_api_wikingrams/
    make run

## Docker containers

Build and run composed docker environment:

    docker-compose build
    docker-compose up
    
To stop your environment press C-c or:

    docker-compose stop

## Checking your application

Check if your API container started successfully:

    curl http://0.0.0.0:5000/healthz

Now you can use curl to check RPC endpoints at 0.0.0.0:5000:

    curl -XPOST -H "Content-type: application/json" -d '{"id": 1, "method": "list_files", "params": []}' http://0.0.0.0:5000/rpc/

You can navigate to main web application using this link:

    open http://0.0.0.0:8001/wikingram/

## License

MIT License. See LICENSE file.
