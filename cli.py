import logic
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    filename='./logs/tictactoe_{time}.log'.format(time=int(time.time())),
                    datefmt='%Y/%m/%d %H:%M:%S',
                    format='%(asctime)s - %(levelname)s - %(filename)s- %(lineno)d  - %(message)s')
logger = logging.getLogger('tictactoe')

if __name__ == '__main__':
    logger.info('game start')
    single = input('game start, single[1], double[2]: ') == '1'
    game = logic.Game(single)
    while True:
        game.turn.do_round()
        game.show_board()
        game.change_turn()
        if game.judge_winner():
            logger.info('game finished')
            break