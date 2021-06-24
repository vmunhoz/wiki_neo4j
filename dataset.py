from model import Article, Person


def build_dataset(db):
    article1 = Article()
    article1.title = "MySQL"
    article1.text = "MySQL is an open-source relational database management system."
    db.graph.push(article1, article4, article5)

    article2 = Article()
    article2.title = "PostgreSQL"
    article2.text = "PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance. It was originally named POSTGRES, referring to its origins as a successor to the Ingres database developed at the University of California, Berkeley."
    # atributo free software?
    db.graph.push(article2)

    article3 = Article()
    article3.title = "Oracle"
    article3.text = "Oracle Database is a multi-model database management system produced and marketed by Oracle Corporation. It is a database commonly used for running online transaction processing, data warehousing and mixed database workloads."
    db.graph.push(article3)

    article4 = Article()
    article4.title = "MariaDB"
    article4.text = "MariaDB is a community-developed, commercially supported fork of the MySQL relational database management system (RDBMS), intended to remain free and open-source software under the GNU General Public License."
    # atributo free software?
    db.graph.push(article1, article5)

    article5 = Article()
    article5.title = "Relational Database"
    article5.text = "A relational database is a digital database based on the relational model of data, as proposed by E. F. Codd in 1970."
    db.graph.push(article3, article6, article2, article7, article8, article4, article9, article10, article11, artcle12)

    article6 = Article()
    article6.title = "Microsoft SQL Server"
    article6.text = "Microsoft SQL Server is a relational database management system developed by Microsoft."
    # atributo free software?
    db.graph.push(article12)

    article7 = Article()
    article7.title = "IBM Db2"
    article7.text = "Db2 is a family of data management products, including database servers, developed by IBM."
    db.graph.push(article5)

    article8 = Article()
    article8.title = "SQLite"
    article8.text = "SQLite is a relational database management system (RDBMS) contained in a C library. In contrast to many other database management systems, SQLite is not a client–server database engine."
    db.graph.push(article5, article2)

    article9 = Article()
    article9.title = "Microsoft Access"
    article9.text = "Microsoft Access is a database management system (DBMS) from Microsoft that combines the relational Microsoft Jet Database Engine with a graphical user interface and software-development tools."
    db.graph.push(article5)

    article10 = Article()
    article10.title = "Hive"
    article10.text = "Apache Hive is a data warehouse software project built on top of Apache Hadoop for providing data query and analysis."
    # atributo free software?
    db.graph.push(article5)

    article11 = Article()
    article11.title = "Teradata"
    article11.text = "Teradata Corporation is a provider of database and analytics-related software, products, and services."
    # db.graph.push(article5)

    article12 = Article()
    article12.title = "Microsoft Azure SQL Database"
    article12.text = "Microsoft Azure SQL Database (formerly SQL Azure, SQL Server Data Services, SQL Services, and Windows Azure SQL Database) is a managed cloud database provided as part of Microsoft Azure."
    db.graph.push(article5)

    # Model
    # articleX = Article()
    # articleX.title =
    # articleX.text =
    # db.graph.push()