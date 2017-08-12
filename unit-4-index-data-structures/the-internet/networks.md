# Networks
A network is a group of entities that can communicate, even though they are **not all directly connected**.

## Not networks:
Each 'node' in these diagrams is directly connected to all other nodes.

![](../images/2017-08-11-15-04-12.png)
![](../images/2017-08-11-15-04-24.png)

## Precise Definiton:
This is a network as the nodes are **not directly conected** but each can **still communicate** with the others.

![](../images/2017-08-11-15-06-01.png)

## Making a Network
* Encoding and interpreting messages
    * Internet (high-level): message-> bits -> electrons/photons 'along wire'.
* Routing messages
    * Internet: Routers 'figure out' next hop.
* Rules for deciding who gets to use resources.
    * i.e. priority for certain people.
    * Internet: Best effort service.
        * No real rules overall.
        * Each router along the network decides on its own which rules to apply.
        * No guarantee a package will reach it's destination - package drops.

## Measuring a Network
### Latency
* Time it takes a message to get from source to destination.
* Unit of time i.e. milliseconds
### Bandwidth
* Amount of information that can be transmitted **per unit time**.
* bps bits per second
* Mbps -> Megabits per second

## Tracing
* `tracert` on windows will trace all the network 'hops' to an endpoint.
![](../images/2017-08-11-15-35-37.png)