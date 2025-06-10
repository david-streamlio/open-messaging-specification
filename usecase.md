# OpenMessaging Common UseCases

This document lists the most of common use cases supported by OpenMessaging.
 
1. P2P
2. Publish/Subscribe
3. Broadcast
4. Highway/assets/images/use_cases
5. Streaming
6. Filter
7. Routing
8. Online Test
9. Upgrade
10. RPC

## P2P

![Point-to-Point.jpg](assets%2Fimages%2Fuse_cases%2FPoint-to-Point.jpg)

P2P, point to point, the simplest one, in this case, Queue is the only involved resource of OpenMessaging which only has one partition. Simply, Producer send message to Queue, and consumed by Consumer later.

## Publish/Subscribe

In this case, Producer send message to Queue with multiple partitions in Round-robin or Hash way. And these partitions will be assigned to consumers who has already subscribed the specified queue regularly.

![PubSub.jpg](assets%2Fimages%2Fuse_cases%2FPubSub.jpg)

Topic and Routing model also can be imported to this case as shown below, if necessary.

![Routing.jpg](assets%2Fimages%2Fuse_cases%2FRouting.jpg)

## Broadcast

![Broadcast.jpg](assets%2Fimages%2Fuse_cases%2FBroadcast.jpg)

In broadcast case, any message sent to the Queue will be consumed by all consumers.

## Highway

![Highway.jpg](assets%2Fimages%2Fuse_cases%2FHighway.jpg)

In highway case, the only focus of SequenceProducer is speed, Producer always want to send abundant and less important messages to Queue. One of the Implementation ways is Batch.

## Streaming

![Streaming.jpg](assets%2Fimages%2Fuse_cases%2FStreaming.jpg)


StreamingConsumer is for this use case, a stream-oriented consumer, to integrate messaging system with Streaming/BigData related platforms easily. StreamingConsumer supports consume messages from partitions of a specified queue like iterator.

## Filter

In most cases, original messages can’t arouse the interests of consumers, and consumers always want to consume processed messages, the most useful processing method is Filter.

As shown below, the Routing model of OpenMessaging can be applied to Filter easily. In this case, the message will be routed to Queue through two filter operators, which will keep the message with Student tag and has a property age between 18~23.

![Filtering.jpg](assets%2Fimages%2Fuse_cases%2FFiltering.jpg)

## Replication

![Replication.jpg](assets%2Fimages%2Fuse_cases%2FReplication.jpg)


Sometimes, the producers and consumers are distributed among multiple data centers, OpenMessaging provides a simple way to route messages from one region to another region.

## Online Test

![Online-Test.jpg](assets%2Fimages%2Fuse_cases%2FOnline-Test.jpg)

Tests are important, many tests like A/B or pressure test need online environment. Create a test Queue with partial traffic can reach this goal.

## Upgrade

![Upgrade.jpg](assets%2Fimages%2Fuse_cases%2FUpgrade.jpg)

Image that we want to release our Consumer version 2.0, which can handle messages with tag Staff or Student, while the version 1.0 consumer only can handle messages with tag Student. OpenMessaging can cover this case easily.

## RPC

![RPC.jpg](assets%2Fimages%2Fuse_cases%2FRPC.jpg)

In OpenMessaging, RPC is equal to synchronous message, it isn’t traditional CS(Client2Server) model, but CSC(Client2Server2Client) model.
