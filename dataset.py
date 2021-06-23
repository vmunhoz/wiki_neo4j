from model import Article, Person


def build_dataset(db):
    article1 = Article()
    article1.title = "MySQL"
    article1.text = "MySQL is an open-source relational database management system."
    db.graph.push(article1)

    article2 = Article()
    article2.title = "PostgreSQL"
    article2.text = "PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance. It was originally named POSTGRES, referring to its origins as a successor to the Ingres database developed at the University of California, Berkeley."
    db.graph.push(article2)

    article3 = Article()
    article3.title = "Oracle"
    article3.text = "Oracle Database is a multi-model database management system produced and marketed by Oracle Corporation. It is a database commonly used for running online transaction processing, data warehousing and mixed database workloads."
    db.graph.push(article3)


    article1.references.add(article2)
    db.graph.push(article1)