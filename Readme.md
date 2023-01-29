# X-I-A API Tutorial - 01-03: Lazy mode and Catalog Object 
## Getting Started

Welcome to XIA API tutorial!

The goal of this tutorial is to quickly show you how to build a complex application by using X-I-A API framework. 
This framework is microservice based in order to get a fast learning curve for developers and AI.

## How to use this tutorial

Each tutorial is ended by a series number like 01-02-03. The longer the series is, the more advanced topic is discussed.
It will be better to finish basic tutorial before going through advanced ones. Each tutorial has example code. 
Installation instruction could be found at tutorial/install.md.

## Prerequisites

Already finish the reading of
* [Tutorial API 01](https://github.com/X-I-A/xia-tutorial-api-01)
* [Tutorial API 01-01](https://github.com/X-I-A/xia-tutorial-api-01-01)
* [Tutorial API 01-02](https://github.com/X-I-A/xia-tutorial-api-01-02)


## Introduction

In this tutorial, you will see a REST based solution for treating three main challenge of API call:
1. No over fetching: You won't get more data than you need
2. No under fetching: You could get data from several data model at one time
3. Progressive loading: You could get the data part by part in asynchronous mode

## Start with example

Please clone and deployed the example code (see [installation guide](tutorial/install.md) for instruction).

Or just visiting the already deployed [online version](https://xia-tutorial-api-01-03-srspyyjtqa-ew.a.run.app/order)

Here is a 1-minute video to show the different solutions

https://user-images.githubusercontent.com/49595269/215358202-1f36d3cb-e9a0-48ab-9e45-6d55ac2ee04a.mp4

Editor maps the call to /api endpoint. /api has much more functionalities and is the real backend entry point.

### Modifications:

Based on the code of [Tutorial API 01-02](https://github.com/X-I-A/xia-tutorial-api-01-02), 
we just do a simple modification:
* models/purchase_order.py:
    * Adding a `CompressStringField` at External Data Model (field `Customer.description`).

CompressStringField is designed to hold a big string in compressed format. Unless is requested, the field will show
its compressed bytes content on base64 format.

## No over fetching

We have defined a data model but not all field is required for a specified application. So it is possible to add a 
catalog object in API call to tell the server which fields are needed.

With the following catalog object, only po_number and order_status are fetched
```
&lazy=false&catalog={"po_number": null, "order_status": null}
```

## No under fetching

There is no need to launch several API call to get data from several data models. 
The data models must have predefined relationship, which is represented by `ExternalField`

With the following catalog object, data from Customer is loaded into PurchaseOrder data model
```
&lazy=false&catalog={"po_number": null, "order_status": null, "customer_detail": {"id": null, "description": null}}
```

You could control the load behavior of each field. We set `customer_detail.description` to true in order to prevent 
decompressing description field. If the value is null, the global lazy setting will be used.
```
&lazy=false&catalog={"po_number": null, "order_status": null, "customer_detail": {"id": null, "description": true}}
```

## Progressive loading

Under fetching is sometimes useful to load progressively a web page. When the External Field is at lazy mode,
the field will provide all the information to load the data in a separate API call. 

Here is the configuration for a progressive loading:
```
&lazy=true&catalog={"po_number": null, "order_status": null, "customer_detail": {"id": null, "description": false}}
```

Based on the given information, it is possible to:
* Loading directly the data (Progressive loading)
* Loading the data only after user's input. For example, after expanding the tree node (Interactive loading)


### Next Step: Making your data persistent

Data Model use by default RamEngine which keeps data in Memory. 
In order to make your data persistent, you will need to change data engine. 
X-I-A is capable of working with any database. Please follow the next tutorial:
* Tutorial 02: Database Engine Integration
* Tutorial 03: User Authentication
* Tutorial 04: Authorization Management
* Tutorial 05: Applying rate limits // Payment
* Tutorial 06: Making independent microservice work as a complex application 
* Tutorial 07: Examples of complex application
