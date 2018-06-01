from configparser import ConfigParser

class GameStats():
    """记录游戏的统计信息"""
    
    def __init__(self, ai_settings):
        super(GameStats, self).__init__()
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # 游戏活动状态
        self.game_active = False
        
        # 最高得分
        self.load_high_score()
        
    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """加载最高分信息"""
        config = ConfigParser()
        conf_name = 'high_score.conf'
        config.read(conf_name, encoding='utf-8')
        try:
            self.high_score = config['highScore'].getint('score', 0)
        except KeyError:
            self.high_score = 0