from ShareAnalysisScipts.db_sqlite import init_db, insert_data
from ShareAnalysisScipts.generator_randomwalk import RandomWalker
from ShareAnalysisScipts.config_Type import WalkerConfig

init_db()
data_id = 0
while data_id <10000:
    config = WalkerConfig()
    rw = RandomWalker(config)
    data_id = rw.SaveWalk()
    print(data_id)