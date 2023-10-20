from sqlalchemy import create_engine
import os

URL_DB=os.getenv("URL_DB")


def query_db(depth_min, grad_min):
    """return wells based on criteria"""
    
    engine=create_engine(URL_DB)

    conn=engine.connect()

    query = f"""SELECT latitude, longitude, depth, gradient
                FROM wells
                WHERE depth > {depth_min} AND gradient > {grad_min}

            """
    results = conn.execute(query).fetchall()

    conn.close()

    return results

if __name__ == '__main__':
    depth_min=2000
    grad_min=0.1
    print(query_db(depth_min, grad_min))
