from wiki_neo4j.model import Article, Person


def build_dataset(db):
    mysql = Article()
    mysql.title = "MySQL"
    mysql.text = "mysql is an open-source relational database management system."
    db.graph.push(mysql)
    # mysql.references.add(postgre, mariadb, relationaldb)

    postgre = Article()
    postgre.title = "PostgreSQL"
    postgre.text = "postgre, also known as Postgres, is a free and open-source relational database management system " \
                   "emphasizing extensibility and SQL compliance. It was originally named POSTGRES, referring to its " \
                   "origins as a successor to the Ingres database developed at the University of California, Berkeley."
    db.graph.push(postgre)
    # postgre.references.add(relationaldb, opensource)

    oracle = Article()
    oracle.title = "Oracle"
    oracle.text = "oracle Database is a multi-model database management system produced and marketed by oracle " \
                  "Corporation. It is a database commonly used for running online transaction processing, data " \
                  "warehousing and mixed database workloads."
    db.graph.push(oracle)
    # oracle.references.add(datawarehouse, postgre, mongodb, neo4j)

    mariadb = Article()
    mariadb.title = "MariaDB"
    mariadb.text = "mariadb is a community-developed, commercially supported fork of the mysql relational database " \
                   "management system (RDBMS), intended to remain free and open-source software under the " \
                   "GNU General Public License."
    db.graph.push(mariadb)
    # mariadb.references.add(mysql, relationaldb, opensource)

    relationaldb = Article()
    relationaldb.title = "Relational Database"
    relationaldb.text = "A relational database is a digital database based on the relational model of data, as " \
                        "proposed by E. F. Codd in 1970."
    db.graph.push(relationaldb)
    # relationaldb.references.add(oracle, mssqlserver, postgre, ibmdb2, sqlite, mariadb, msaccess, hive, teradata,
    # msazure)

    mssqlserver = Article()
    mssqlserver.title = "Microsoft SQL Server"
    mssqlserver.text = "Microsoft SQL Server is a relational database management system developed by Microsoft."
    db.graph.push(mssqlserver)
    # mssqlserver.references.add(msazure, opensource)

    ibmdb2 = Article()
    ibmdb2.title = "IBM Db2"
    ibmdb2.text = "Db2 is a family of data management products, including database servers, developed by IBM."
    db.graph.push(ibmdb2)
    # ibmdb2.references.add(relationaldb)

    sqlite = Article()
    sqlite.title = "SQLite"
    sqlite.text = "SQLite is a relational database management system (RDBMS) contained in a C library. In contrast " \
                  "to many other database management systems, SQLite is not a client–server database engine."
    db.graph.push(sqlite)
    # sqlite.references.add(relationaldb, postgre)

    msaccess = Article()
    msaccess.title = "Microsoft Access"
    msaccess.text = "Microsoft Access is a database management system (DBMS) from Microsoft that combines the " \
                    "relational Microsoft Jet Database Engine with a graphical user interface and " \
                    "software-development tools."
    db.graph.push(msaccess)
    # msaccess.references.add(relationaldb)

    hive = Article()
    hive.title = "Hive"
    hive.text = "Apache Hive is a data warehouse software project built on top of Apache Hadoop for providing data " \
                "query and analysis."
    # atributo free software?
    db.graph.push(hive)
    # hive.references.add(relationaldb)

    teradata = Article()
    teradata.title = "Teradata"
    teradata.text = "Teradata Corporation is a provider of database and analytics-related software, products, " \
                    "and services."
    db.graph.push(teradata)
    # teradata.references.add(relationaldb)

    msazure = Article()
    msazure.title = "Microsoft Azure SQL Database"
    msazure.text = "Microsoft Azure SQL Database (formerly SQL Azure, SQL Server Data Services, SQL Services, " \
                   "and Windows Azure SQL Database) is a managed cloud database provided as part of Microsoft Azure."
    db.graph.push(msazure)
    # msazure.references.add(relationaldb)

    # Others

    opensource = Article()
    opensource.title = "Open-source software"
    opensource.text = "Open-source software (OSS) is computer software that is released under a license in which " \
                      "the copyright holder grants users the rights to use, study, change, and distribute the " \
                      "software and its source code to anyone and for any purpose."
    db.graph.push(opensource)
    # opensource.references.add(postgre, mariadb, mssqlserver, flockdb, cassandra, hbase, foundationdb, leveldb,
    # riak, couchdb, tokumx)

    graphdb = Article
    graphdb.title = "Graph database"
    graphdb.text = "In computing, a graph database (GDB) is a database that uses graph structures for semantic " \
                   "queries with nodes, edges, and properties to represent and store data."
    db.graph.push(graphdb)
    # graphdb.references.add(relationaldb, nosql, infinitegraph)

    datawarehouse = Article
    datawarehouse.title = "Data warehouse"
    datawarehouse.text = "In computing, a data warehouse (DW or DWH), also known as an enterprise data warehouse " \
                         "(EDW), is a system used for reporting and data analysis and is considered a core " \
                         "component of business intelligence."
    db.graph.push(datawarehouse)
    # datawarehouse.references.add()

    # NoSQL #
    nosql = Article()
    nosql.title = "NoSQL"
    nosql.text = "A NoSQL (originally referring to 'non-SQL' or 'non-relational') database provides a mechanism " \
                 "for storage and retrieval of data that is modeled in means other than the tabular relations " \
                 "used in relational databases."
    db.graph.push(nosql)
    # nosql.references.add(allegrograph, neptune, arangodb, cosmosdb, dexsparksee, flockdb, ibmdb2, infinitegraph,
    #                   marklogic, neo4j, oracle, virtuoso, orientdb, mongodb, cassandra, hbase, dynamodb, aerospike,
    #                   ignite, foundationdb, hazelcast, hibari, infinitydb, leveldb, oraclenosql, voldemort, redis,
    #                   riak, rocksdb, basex, cloudant, couchdb, simpledb, tokumx)

    # Graph
    allegrograph = Article()
    allegrograph.title = "AllegroGraph"
    allegrograph.text = "AllegroGraph is a closed source triplestore which is designed to store RDF triples, " \
                        "a standard format for Linked Data.  It also operates as a document store designed " \
                        "for storing, retrieving and managing document-oriented information, in JSON-LD format."
    db.graph.push(allegrograph)
    # allegrograph.references.add(nosql, graphdb)

    neptune = Article()
    neptune.title = "Amazon Neptune"
    neptune.text = "Amazon Neptune is a managed graph database product published by Amazon.com."
    db.graph.push(neptune)
    # neptune.references.add(nosql, graphdb)

    arangodb = Article()
    arangodb.title = "ArangoDB"
    arangodb.text = "ArangoDB is a free and open-source native multi-model database system developed by ArangoDB GmbH."
    db.graph.push(arangodb)
    # arangodb.references.add(opensource, nosql, graphdb, keyvalue)

    cosmosdb = Article()
    cosmosdb.title = "Azure Cosmos DB"
    cosmosdb.text = "Azure Cosmos DB is Microsoft's proprietary globally-distributed, multi-model database " \
                    "service 'for managing data at planet-scale' launched in May 2017.  It is schema-agnostic," \
                    "horizontally scalable, and generally classified as a NoSQL database."
    db.graph.push(cosmosdb)
    # cosmosdb.references.add(nosql, graphdb)

    dexsparksee = Article()
    dexsparksee.title = "DEX/Sparksee"
    dexsparksee.text = "Sparksee (formerly known as DEX) is a high-performance and scalable graph database " \
                       "management system written in C++. "
    db.graph.push(dexsparksee)
    # dexsparksee.references.add(nosql, graphdb)

    flockdb = Article()
    flockdb.title = "FlockDB"
    flockdb.text = "FlockDB is an open-source distributed, fault-tolerant graph database for managing wide but " \
                   "shallow network graphs."
    db.graph.push(flockdb)
    # flockdb.references.add(nosql, graphdb, opensource)

    infinitegraph = Article()
    infinitegraph.title = "InfiniteGraph"
    infinitegraph.text = "InfiniteGraph is a distributed graph database implemented in Java and C++ and is from a " \
                         "class of NOSQL ('Not Only SQL') database technologies that focus on graph data structures."
    db.graph.push(infinitegraph)
    # infinitegraph.references.add(nosql, graphdb)

    marklogic = Article()
    marklogic.title = "MarkLogic"
    marklogic.text = "MarkLogic is a multi-model NoSQL database that has evolved from its XML database roots to " \
                     "also natively store JSON documents and RDF triples for its semantic data model. It uses " \
                     "a distributed architecture that can handle hundreds of billions of documents and " \
                     "hundreds of terabytes of data."
    db.graph.push(marklogic)
    # .references.add(nosql, datawarehouse, graphdb, mongodb)

    neo4j = Article()
    neo4j.title = "Neo4j"
    neo4j.text = "Neo4j is a graph database management system developed by Neo4j, Inc."
    db.graph.push(neo4j)
    # neo4j.references.add(nosql, graphdb)

    virtuoso = Article()
    virtuoso.title = "OpenLink Virtuoso"
    virtuoso.text = "Virtuoso Universal Server is a middleware and database engine hybrid that combines the " \
                    "functionality of a traditional relational database management system (RDBMS), " \
                    "object–relational database (ORDBMS), virtual database, RDF, XML, free-text, web application " \
                    "server and file server functionality in a single system."
    db.graph.push(virtuoso)
    # virtuoso.references.add(relationaldb, nosql, graphdb, keyvalue)

    orientdb = Article()
    orientdb.title = "OrientDB"
    orientdb.text = "OrientDB is an open source NoSQL database management system written in Java. It is a " \
                    "Multi-model database, supporting graph, document, key/value, and object models, but the " \
                    "relationships are managed as in graph databases with direct connections between records."
    db.graph.push(orientdb)
    # orientdb.references.add(nosql, graphdb)

# Others

    mongodb = Article()
    mongodb.title = "MongoDB"
    mongodb.text = "MongoDB is a source-available cross-platform document-oriented database program. Classified " \
                   "as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas."
    db.graph.push(nosql)
    # mongodb.references.add(nosql)

    cassandra = Article()
    cassandra.title = "Apache Cassandra"
    cassandra.text = "Apache Cassandra is a free and open-source, distributed, wide-column store, NoSQL database " \
                     "management system designed to handle large amounts of data across many commodity servers, " \
                     "providing high availability with no single point of failure."
    db.graph.push(cassandra)
    # cassandra.references.add(nosql, opensource)

    hbase = Article()
    hbase.title = "Apache HBase"
    hbase.text = "HBase is an open-source non-relational distributed database modeled after Google's Bigtable " \
                 "and written in Java. It is developed as part of Apache Software Foundation's Apache Hadoop " \
                 "project and runs on top of HDFS (Hadoop Distributed File System) or Alluxio, providing " \
                 "Bigtable-like capabilities for Hadoop."
    db.graph.push(hbase)
    # hbase.references.add(nosql, opensource, mongodb, dynamodb)

    dynamodb = Article()
    dynamodb.title = "Amazon DynamoDB"
    dynamodb.text = "Amazon DynamoDB is a fully managed proprietary NoSQL database service that supports key–value " \
                    "and document data structures and is offered by Amazon.com as part of the " \
                    "Amazon Web Services portfolio."
    db.graph.push(dynamodb)
    # dynamodb.references.add(nosql, mongodb)

    # Key-value database

    keyvalue = Article()
    keyvalue.title = "Key–value database"
    keyvalue.text = "A key–value database, or key–value store, is a data storage paradigm designed for storing, " \
                    "retrieving, and managing associative arrays, and a data structure more commonly known today " \
                    "as a dictionary or hash table. Dictionaries contain a collection of objects, or records, " \
                    "which in turn have many different fields within them, each containing data. " \
                    "These records are stored and retrieved using a key that uniquely identifies the record, " \
                    "and is used to find the data within the database."
    db.graph.push(keyvalue)
    # keyvalue.references.add(aerospike, ignite, arangodb, foundationdb, hazelcast, hibari, infinitydb, leveldb,
    # oraclenosql, voldemort, redis, riak, rocksdb, virtuoso)

    redis = Article()
    redis.title = "Redis"
    redis.text = "Redis (Remote Dictionary Server) is an in-memory data structure store, used as a distributed, " \
                 "in-memory key–value database, cache and message broker, with optional durability. Redis supports " \
                 "different kinds of abstract data structures, such as strings, lists, maps, sets, sorted sets, " \
                 "HyperLogLogs, bitmaps, streams, and spatial indices."
    db.graph.push(redis)
    # redis.references.add(nosql, keyvalue)

    aerospike = Article()
    aerospike.title = "Aerospike"
    aerospike.text = "Aerospike is a flash-optimized and in-memory open source distributed key value NoSQL database, " \
                     "and the name of the eponymous company that produces it."
    db.graph.push(aerospike)
    # aerospike.references.add(nosql, mongodb)

    ignite = Article()
    ignite.title = "Apache Ignite"
    ignite.text = "Apache Ignite is a distributed database for high-performance computing with in-memory speed. " \
                  "Apache Ignite's database utilizes RAM as the default storage and processing tier, thus, " \
                  "belonging to the class of in-memory computing platforms. The disk tier is optional but, " \
                  "once enabled, will hold the full data set whereas the memory tier will cache full or partial " \
                  "data set depending on its capacity."
    db.graph.push(ignite)
    # ignite.references.add(nosql, keyvalue)

    foundationdb = Article()
    foundationdb.title = "FoundationDB"
    foundationdb.text = "FoundationDB is a free and open-source multi-model distributed NoSQL database developed " \
                        "by Apple Inc. with a shared-nothing architecture. The product was designed around a " \
                        "'core' database, with additional features supplied in 'layers'."
    db.graph.push(foundationdb)
    # foundationdb.references.add(nosql, keyvalue, opensource)

    hazelcast = Article()
    hazelcast.title = "Hazelcast"
    hazelcast.text = "In computing, Hazelcast IMDG is an open source in-memory data grid based on Java. " \
                     "In a Hazelcast grid, data is evenly distributed among the nodes of a computer cluster, " \
                     "allowing for horizontal scaling of processing and available storage."
    db.graph.push(hazelcast)
    # hazelcast.references.add(nosql, keyvalue)

    hibari = Article()
    hibari.title = "Hibari"
    hibari.text = "Hibari is a strongly consistent, highly available, distributed, key-value Big Data store."
    db.graph.push(hibari)
    # hibari.references.add(nosql, keyvalue)

    infinitydb = Article()
    infinitydb.title = "InfinityDB"
    infinitydb.text = "InfinityDB is an all-Java embedded database engine and client/server DBMS with an extended " \
                      "java.util.concurrent.ConcurrentNavigableMap interface that is deployed in handheld devices, " \
                      "on servers, on workstations, and in distributed settings. The design is based on a " \
                      "proprietary lockless, concurrent, B-tree architecture that enables client programmers " \
                      "to reach high levels of performance without risk of failures."
    db.graph.push(infinitydb)
    # infinitydb.references.add(nosql, keyvalue)

    leveldb = Article()
    leveldb.title = "LevelDB"
    leveldb.text = "LevelDB is an open-source on-disk key-value store written by Google fellows Jeffrey Dean and " \
                   "Sanjay Ghemawat. Inspired by Bigtable, LevelDB is hosted on GitHub under the New BSD " \
                   "License and has been ported to a variety of Unix-based systems, and macOS, Windows, and Android."
    db.graph.push(leveldb)
    # leveldb.references.add(nosql, keyvalue, opensource)

    voldemort = Article()
    voldemort.title = "Voldemort (distributed data store)"
    voldemort.text = "Voldemort is a distributed data store that was designed as a key-value store used by " \
                     "LinkedIn for highly-scalable storage. It is named after the fictional Harry Potter " \
                     "villain Lord Voldemort."
    db.graph.push(voldemort)
    # keyvalue.references.add(nosql, keyvalue)

    riak = Article()
    riak.title = "Riak"
    riak.text = "Riak is a distributed NoSQL key-value data store that offers high availability, fault tolerance, " \
                "operational simplicity, and scalability. In addition to the open-source version, " \
                "it comes in a supported enterprise version and a cloud storage version."
    db.graph.push(riak)
    # riak.references.add(nosql, keyvalue, opensource, dynamodb, leveldb)

    rocksdb = Article()
    rocksdb.title = "RocksDB"
    rocksdb.text = "RocksDB is a high performance[2][3][4][5][6] embedded database for key-value data. " \
                   "It is a fork of Google's LevelDB optimized to exploit many CPU cores, and make efficient " \
                   "use of fast storage, such as solid-state drives (SSD), for input/output (I/O) bound workloads."
    db.graph.push(rocksdb)
    # rocksdb.references.add(nosql, keyvalue, leveldb)

    oraclenosql = Article()
    oraclenosql.title = "Oracle NoSQL Database"
    oraclenosql.text = "Oracle NoSQL Database (ONDB) is a NoSQL-type distributed key-value database from " \
                       "Oracle Corporation. It provides transactional semantics for data manipulation, " \
                       "horizontal scalability, and simple administration and monitoring."
    db.graph.push(oraclenosql)
    # oraclenosql.references.add(nosql, keyvalue)

    # Document-oriented database
    documentdb = Article()
    documentdb.title = "Document-oriented database"
    documentdb.text = "A document-oriented database, or document store, is a computer program and data storage " \
                      "system designed for storing, retrieving and managing document-oriented information, " \
                      "also known as semi-structured data."
    db.graph.push(documentdb)
    # documentdb.references.add(nosql, graphdb, keyvalue, relationaldb, mongodb, aerospike, allegro, arangodb,
    # cosmosdb, marklogic, virtuoso, oraclenosql, postgre, basex, cloudant, couchdb, simpledb, tokumx)

    basex = Article()
    basex.title = "BaseX"
    basex.text = "BaseX is a native and light-weight XML database management system and XQuery processor, " \
                 "developed as a community project on GitHub. It is specialized in storing, querying, and " \
                 "visualizing large XML documents and collections."
    db.graph.push(basex)
    # basex.references.add(nosql, documentdb)

    cloudant = Article()
    cloudant.title = "Cloudant"
    cloudant.text = "Cloudant is an IBM software product, which is primarily delivered as a cloud-based service. " \
                    "Cloudant is a non-relational, distributed database service of the same name. Cloudant is " \
                    "based on the Apache-backed CouchDB project and the open source BigCouch project."
    db.graph.push()
    # cloudant.references.add(nosql, documentdb, couchdb)

    couchdb = Article()
    couchdb.title = "Apache CouchDB"
    couchdb.text = "Apache CouchDB is an open-source document-oriented NoSQL database, implemented in Erlang. " \
                   "CouchDB uses multiple formats and protocols to store, transfer, and process its data. " \
                   "It uses JSON to store data, JavaScript as its query language using MapReduce, " \
                   "and HTTP for an API."
    db.graph.push(couchdb)
    # couchdb.references.add(nosql, documentdb)

    simpledb = Article()
    simpledb.title = "Amazon SimpleDB"
    simpledb.text = "Amazon SimpleDB is a distributed database written in Erlang by Amazon.com. " \
                    "It is used as a web service in concert with Amazon Elastic Compute Cloud (EC2) and " \
                    "Amazon S3 and is part of Amazon Web Services. It was announced on December 13, 2007."
    db.graph.push()
    # simpledb.references.add(nosql, documentdb, dynamodb)

    tokumx = Article()
    tokumx.title = "TokuMX"
    tokumx.text = "TokuMX is an open-source distribution of MongoDB which, among other things, replaces the " \
                  "default B-tree data structure found in the basic MongoDB distribution with a Fractal Tree index."
    db.graph.push()
    # tokumx.references.add(nosql, documentdb, mongodb)

    # Model
    # articleX = Article()
    # articleX.title =
    # articleX.text =
    # db.graph.push()

    # mysql.references.add(postgre)
    # db.graph.push(mysql)

    # Article references
    # Relational
    mysql.references.add(postgre, mariadb, relationaldb)
    postgre.references.add(relationaldb, opensource)
    oracle.references.add(datawarehouse, postgre, mongodb, neo4j)
    mariadb.references.add(mysql, relationaldb, opensource)
    relationaldb.references.add(oracle, mssqlserver, postgre, ibmdb2, sqlite, mariadb, msaccess, hive, teradata,
                                msazure)
    mssqlserver.references.add(msazure, opensource)
    ibmdb2.references.add(relationaldb)
    sqlite.references.add(relationaldb, postgre)
    msaccess.references.add(relationaldb)
    hive.references.add(relationaldb)
    teradata.references.add(relationaldb)
    msazure.references.add(relationaldb)

    # Others
    opensource.references.add(postgre, mariadb, mssqlserver, flockdb, cassandra, hbase, foundationdb, leveldb, riak,
                              couchdb, tokumx)
    graphdb.references.add(relationaldb, nosql, infinitegraph)
    datawarehouse.references.add()

    # NoSQL
    nosql.references.add(allegrograph, neptune, arangodb, cosmosdb, dexsparksee, flockdb, ibmdb2, infinitegraph,
                         marklogic, neo4j,
                         oracle, virtuoso, orientdb, mongodb, cassandra, hbase, dynamodb, aerospike, ignite,
                         foundationdb, hazelcast,
                         hibari, infinitydb, leveldb, oraclenosql, voldemort, redis, riak, rocksdb, basex, cloudant,
                         couchdb, simpledb, tokumx)
    # Graph
    allegrograph.references.add(nosql, graphdb)
    neptune.references.add(nosql, graphdb)
    arangodb.references.add(opensource, nosql, graphdb)
    cosmosdb.references.add(nosql, graphdb)
    dexsparksee.references.add(nosql, graphdb)
    flockdb.references.add(nosql, graphdb, opensource)
    infinitegraph.references.add(nosql, graphdb)
    marklogic.references.add(nosql, datawarehouse, graphdb, mongodb)
    neo4j.references.add(nosql, graphdb)
    virtuoso.references.add(relationaldb, nosql, graphdb)
    orientdb.references.add(nosql, graphdb)
    mongodb.references.add(nosql)
    cassandra.references.add(nosql, opensource)
    hbase.references.add(nosql, opensource, mongodb, dynamodb)
    dynamodb.references.add(nosql, mongodb)
    # Key-value
    keyvalue.references.add(aerospike, ignite, arangodb, foundationdb, hazelcast, hibari, infinitydb, leveldb,
                            oraclenosql, voldemort, redis, riak, rocksdb, virtuoso)
    redis.references.add(nosql, keyvalue)
    aerospike.references.add(nosql, mongodb)
    ignite.references.add(nosql, keyvalue)
    foundationdb.references.add(nosql, keyvalue, opensource)
    hazelcast.references.add(nosql, keyvalue)
    hibari.references.add(nosql, keyvalue)
    infinitydb.references.add(nosql, keyvalue)
    leveldb.references.add(nosql, keyvalue, opensource)
    keyvalue.references.add(nosql, keyvalue)
    riak.references.add(nosql, keyvalue, opensource, dynamodb, leveldb)
    rocksdb.references.add(nosql, keyvalue, leveldb)
    oraclenosql.references.add(nosql, keyvalue)
    # Document
    documentdb.references.add(nosql, graphdb, keyvalue, relationaldb, mongodb, aerospike, allegrograph, arangodb,
                              cosmosdb, marklogic, virtuoso, oraclenosql, postgre, basex, cloudant, couchdb, simpledb,
                              tokumx)
    basex.references.add(nosql, documentdb)
    cloudant.references.add(nosql, documentdb, couchdb)
    couchdb.references.add(nosql, documentdb)
    simpledb.references.add(nosql, documentdb, dynamodb)
    tokumx.references.add(nosql, documentdb, mongodb)

    # Person related to article
    hanay = Person()
    hanay.name = "Hanay"

    henrique = Person()
    henrique.name = "Henrique"

    vinicius = Person()
    vinicius.name = "Vinicius"

    ricardo = Person()
    ricardo.name = "Ricardo"

    fillipe = Person()
    fillipe.name = "Fillipe"

    rodolfo = Person()
    rodolfo.name = "Rodolfo"

    andre = Person()
    andre.name = "Andre"

    ligia = Person()
    ligia.name = "Ligia"

    gabriel = Person()
    gabriel.name = "Gabriel"

    helio = Person()
    helio.name = "Helio"

    lais = Person()
    lais.name = "Lais"

    monica = Person()
    monica.name = "Monica"

    # Person
    hanay.likes.add(dexsparksee, tokumx, aerospike, hibari, hazelcast)
    henrique.likes.add(mysql, mssqlserver, marklogic, redis, ignite, leveldb, documentdb)
    vinicius.likes.add(oracle, cosmosdb, mongodb, cassandra, voldemort, infinitydb, simpledb)
    ricardo.likes.add(relationaldb, graphdb, datawarehouse, nosql, keyvalue)
    fillipe.likes.add(arangodb, orientdb, hbase)
    rodolfo.likes.add(opensource)
    andre.likes.add(postgre, hive, riak)
    ligia.likes.add(sqlite, neptune, foundationdb, rocksdb)
    gabriel.likes.add(ibmdb2, teradata, dynamodb)
    helio.likes.add(mariadb, virtuoso)
    lais.likes.add(allegrograph, neo4j, flockdb, infinitegraph, basex)
    monica.likes.add(msaccess, msazure, oraclenosql, cloudant, couchdb)
