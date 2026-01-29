## Creational design pattern focus how object are created. 
Instead of Scattering ClassName() everywhere, Hard-coding object creation 
Tightly couple the code to object creation 
Creational patterns control, abstract, or optimize object creation.

In simple words: They decide who create the object, how it's created, and when

Creational Design pattern is used when object creation logic is 
* Abstracted
* Controlled 
* Delegated 

Single Tone design pattern - Only one instance should exist. 
Multiple instance can cause inconsistency.

Application Example of Singletone design pattern
1. SparkSession 
    spark = SparkSession.builder.appName("TestApp").getOrCreate()
    Get of Create mean - if there is existing session then return that 
    else create one and return. So there is one and only one session throughout 
    the life-cycle of the application
    Metal Model = One Driver = one SparkSession = one brain
2. Airflow — DAGBag & Scheduler (Implicit Singleton)
    Only one scheduler should assign tasks. Scheduler is effectively a singletone.
    Scheduler → reads DAGs → decides task state. 
    If there is multiple instance of scheduler - same task can be scheduled multiple times.
    Which can cause multiple job execution and data corruption etc. 
3. Database Connection Pool — Pool Manager
    A singletone database connection pool can manager mulitple connections. 
    Hands them out safely, reuses connection 
    If multiple pool managers exist: Each creates its own connections, 
    DB connection limit exceeded, APP crashes 
4.  Metadata / Schema Registry (Data Platforms):
    Real systems: Hive metastore, Clue Catalog, Confluent Schema Registry 
    One authoritative schema source. Multiple registries= schema drifts 
    In case multiple : Producer writes schema v2 and Consumer reads schema v1
5. Feature Store Client (ML / DE overlap)
    Why Singleton: Consistent feature definitions , Shared caching and Controlled acces;
    Without a singletone: Multiple clients: Cache mismatch, Training & inference skew

These systems don’t always implement Singleton in code —
they enforce it via:
* Locks 
* Leader election
* External state (DB, Zookeeper, etcd)



 
