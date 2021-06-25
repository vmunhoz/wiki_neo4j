from model import Article, Person


def build_dataset(db):
    mysql = Article()
    mysql.title = "MySQL"
    mysql.text = "mysql is an open-source relational database management system."
    db.graph.push(mysql)
    # mysql.references.add(postgre, mariadb, relationaldb)

    postgre = Article()
    postgre.title = "PostgreSQL"
    postgre.text = "postgre, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance. It was originally named POSTGRES, referring to its origins as a successor to the Ingres database developed at the University of California, Berkeley."
    db.graph.push(postgre)
    # postgre.references.add(relationaldb, opensource)

    oracle = Article()
    oracle.title = "Oracle"
    oracle.text = "oracle Database is a multi-model database management system produced and marketed by oracle Corporation. It is a database commonly used for running online transaction processing, data warehousing and mixed database workloads."
    db.graph.push(oracle)
    # oracle.references.add(datawarehouse, postgre, mongodb, neo4j)

    mariadb = Article()
    mariadb.title = "MariaDB"
    mariadb.text = "mariadb is a community-developed, commercially supported fork of the mysql relational database management system (RDBMS), intended to remain free and open-source software under the GNU General Public License."
    db.graph.push(mariadb)
    # mariadb.references.add(mysql, relationaldb, opensource)

    relationaldb = Article()
    relationaldb.title = "Relational Database"
    relationaldb.text = "A relational database is a digital database based on the relational model of data, as proposed by E. F. Codd in 1970."
    db.graph.push(relationaldb)
    # relationaldb.references.add(oracle, mssqlserver, postgre, ibmdb2, sqlite, mariadb, msaccess, hive, teradata, msazure)

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
    sqlite.text = "SQLite is a relational database management system (RDBMS) contained in a C library. In contrast to many other database management systems, SQLite is not a client–server database engine."
    db.graph.push(sqlite)
    # sqlite.references.add(relationaldb, postgre)

    msaccess = Article()
    msaccess.title = "Microsoft Access"
    msaccess.text = "Microsoft Access is a database management system (DBMS) from Microsoft that combines the relational Microsoft Jet Database Engine with a graphical user interface and software-development tools."
    db.graph.push(msaccess)
    # msaccess.references.add(relationaldb)

    hive = Article()
    hive.title = "Hive"
    hive.text = "Apache Hive is a data warehouse software project built on top of Apache Hadoop for providing data query and analysis."
    # atributo free software?
    db.graph.push(hive)
    # hive.references.add(relationaldb)

    teradata = Article()
    teradata.title = "Teradata"
    teradata.text = "Teradata Corporation is a provider of database and analytics-related software, products, and services."
    db.graph.push(teradata)
    # teradata.references.add(relationaldb)

    msazure = Article()
    msazure.title = "Microsoft Azure SQL Database"
    msazure.text = "Microsoft Azure SQL Database (formerly SQL Azure, SQL Server Data Services, SQL Services, and Windows Azure SQL Database) is a managed cloud database provided as part of Microsoft Azure."
    db.graph.push(msazure)
    # msazure.references.add(relationaldb)

### ### ###

    opensource = Article()
    opensource.title = "Open-source software"
    opensource.text = "Open-source software (OSS) is computer software that is released under a license in which the copyright holder grants users the rights to use, study, change, and distribute the software and its source code to anyone and for any purpose."
    db.graph.push(opensource)
    # opensource.references.add(postgre, mariadb, mssqlserver, flockdb, cassandra, hbase)

    graphdb = Article
    graphdb.title = "Graph database"
    graphdb.text = "In computing, a graph database (GDB) is a database that uses graph structures for semantic queries with nodes, edges, and properties to represent and store data."
    db.graph.push(graphdb)
    # graphdb.references.add(relationaldb, nosql, infinitegraph)

    datawarehouse = Article
    datawarehouse.title = "Data warehouse"
    datawarehouse.text = "In computing, a data warehouse (DW or DWH), also known as an enterprise data warehouse (EDW), is a system used for reporting and data analysis and is considered a core component of business intelligence."
    db.graph.push(datawarehouse)
    # datawarehouse.references.add()

### NoSQL ###
    nosql = Article()
    nosql.title = "NoSQL"
    nosql.text = "A NoSQL (originally referring to 'non-SQL' or 'non-relational') database provides a mechanism for storage and retrieval of data that is modeled in means other than the tabular relations used in relational databases."
    db.graph.push(nosql)
    # nosql.references.add(allegrograph, neptune, arangodb, cosmosdb, dexsparksee, flockdb, ibmdb2, infinitegraph, marklogic, neo4j,
    #                   oracle, virtuoso, orientdb, mongodb, cassandra, hbase, dynamodb)

# Graph
    allegrograph = Article()
    allegrograph.title = "AllegroGraph"
    allegrograph.text = "AllegroGraph is a closed source triplestore which is designed to store RDF triples, a standard format for Linked Data.  It also operates as a document store designed for storing, retrieving and managing document-oriented information, in JSON-LD format."
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
    # arangodb.references.add(opensource, nosql, graphdb)

    cosmosdb = Article()
    cosmosdb.title = "Azure Cosmos DB"
    cosmosdb.text = "Azure Cosmos DB is Microsoft's proprietary globally-distributed, multi-model database service 'for managing data at planet-scale' launched in May 2017.  It is schema-agnostic, horizontally scalable, and generally classified as a NoSQL database."
    db.graph.push(cosmosdb)
    # cosmosdb.references.add(nosql, graphdb)

    dexsparksee = Article()
    dexsparksee.title = "DEX/Sparksee"
    dexsparksee.text = "Sparksee (formerly known as DEX) is a high-performance and scalable graph database management system written in C++. "
    db.graph.push(dexsparksee)
    # dexsparksee.references.add(nosql, graphdb)

    flockdb = Article()
    flockdb.title = "FlockDB"
    flockdb.text = "FlockDB is an open-source distributed, fault-tolerant graph database for managing wide but shallow network graphs."
    db.graph.push(flockdb)
    # flockdb.references.add(nosql, graphdb, opensource)

    infinitegraph = Article()
    infinitegraph.title = "InfiniteGraph"
    infinitegraph.text = "InfiniteGraph is a distributed graph database implemented in Java and C++ and is from a class of NOSQL ('Not Only SQL') database technologies that focus on graph data structures."
    db.graph.push(infinitegraph)
    # infinitegraph.references.add(nosql, graphdb)

    marklogic = Article()
    marklogic.title = "MarkLogic"
    marklogic.text = "MarkLogic is a multi-model NoSQL database that has evolved from its XML database roots to also natively store JSON documents and RDF triples for its semantic data model. It uses a distributed architecture that can handle hundreds of billions of documents and hundreds of terabytes of data."
    db.graph.push(marklogic)
    # .references.add(nosql, datawarehouse, graphdb, mongodb)

    neo4j = Article()
    neo4j.title = "Neo4j"
    neo4j.text = "Neo4j is a graph database management system developed by Neo4j, Inc."
    db.graph.push(neo4j)
    # neo4j.references.add(nosql, graphdb)

    virtuoso = Article()
    virtuoso.title = "OpenLink Virtuoso"
    virtuoso.text = "Virtuoso Universal Server is a middleware and database engine hybrid that combines the functionality of a traditional relational database management system (RDBMS), object–relational database (ORDBMS), virtual database, RDF, XML, free-text, web application server and file server functionality in a single system."
    db.graph.push(virtuoso)
    # virtuoso.references.add(relationaldb, nosql, graphdb)

    orientdb = Article()
    orientdb.title = "OrientDB"
    orientdb.text = "OrientDB is an open source NoSQL database management system written in Java. It is a Multi-model database, supporting graph, document, key/value, and object models, but the relationships are managed as in graph databases with direct connections between records."
    db.graph.push(orientdb)
    # orientdb.references.add(nosql, graphdb)

# Others

    mongodb = Article()
    mongodb.title = "MongoDB"
    mongodb.text = "MongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas."
    db.graph.push(nosql)
    # mongodb.references.add(nosql)

    cassandra = Article()
    cassandra.title = "Apache Cassandra"
    cassandra.text = "Apache Cassandra is a free and open-source, distributed, wide-column store, NoSQL database management system designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure."
    db.graph.push(cassandra)
    # cassandra.references.add(nosql, opensource)

    hbase = Article()
    hbase.title = "Apache HBase"
    hbase.text = "HBase is an open-source non-relational distributed database modeled after Google's Bigtable and written in Java. It is developed as part of Apache Software Foundation's Apache Hadoop project and runs on top of HDFS (Hadoop Distributed File System) or Alluxio, providing Bigtable-like capabilities for Hadoop."
    db.graph.push(hbase)
    # hbase.references.add(nosql, opensource, mongodb, dynamodb)

    dynamodb = Article()
    dynamodb.title = "Amazon DynamoDB"
    dynamodb.text = "Amazon DynamoDB is a fully managed proprietary NoSQL database service that supports key–value and document data structures and is offered by Amazon.com as part of the Amazon Web Services portfolio."
    db.graph.push(dynamodb)
    # dynamodb.references.add(nosql, mongodb)


    # Graphdb e opensource como atributo ao invés de conexão?

    # Model
    # articleX = Article()
    # articleX.title =
    # articleX.text =
    # db.graph.push()

    # mysql.references.add(postgre)
    # db.graph.push(mysql)

    mysql.references.add(postgre, mariadb, relationaldb)
    postgre.references.add(relationaldb, opensource)
    oracle.references.add(datawarehouse, postgre, mongodb, neo4j)
    mariadb.references.add(mysql, relationaldb, opensource)
    relationaldb.references.add(oracle, mssqlserver, postgre, ibmdb2, sqlite, mariadb, msaccess, hive, teradata, msazure)
    mssqlserver.references.add(msazure, opensource)
    ibmdb2.references.add(relationaldb)
    sqlite.references.add(relationaldb, postgre)
    msaccess.references.add(relationaldb)
    hive.references.add(relationaldb)
    teradata.references.add(relationaldb)
    msazure.references.add(relationaldb)

    opensource.references.add(postgre, mariadb, mssqlserver, flockdb, cassandra, hbase)
    graphdb.references.add(relationaldb, nosql, infinitegraph)
    datawarehouse.references.add()
    nosql.references.add(allegrograph, neptune, arangodb, cosmosdb, dexsparksee, flockdb, ibmdb2, infinitegraph, marklogic, neo4j,
                         oracle, virtuoso, orientdb, mongodb, cassandra, hbase, dynamodb)

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
