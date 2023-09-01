import time
from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from prometheus_client import REGISTRY


# Define the Prometheus metrics
REQUEST_COUNT = Counter('request_count', 'Total number of requests')
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency in seconds')


# Define the middleware to track the metrics
async def track_requests(request, call_next):
    # Increment the request count
    REQUEST_COUNT.inc()

    # Record the start time
    start_time = time.time()

    # Call the next middleware or the endpoint handler
    response = await call_next(request)

    # Record the end time and calculate the request latency
    end_time = time.time()
    latency = end_time - start_time

    # Record the request latency
    REQUEST_LATENCY.observe(latency)

    return response


# Define the endpoint to expose the metrics




# The FastAPI instance is created.
# Two Prometheus metrics (request_count and request_latency_seconds) are 
# defined using the Counter and Histogram classes from the prometheus_client library.
# A middleware function (track_requests) is defined that increments the request count and records the request latency.
# An endpoint (/metrics) is defined that exposes the metrics in a format that Prometheus can scrape.

# This code defines two Prometheus metrics (request_count and request_latency_seconds) and a 
# middleware function (track_requests) that increments the request count and records the request latency. 
# The code also defines an endpoint (/metrics) that exposes the metrics in a format that Prometheus can scrape.