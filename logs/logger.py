import logging
from lightgbm.callback import _format_eval_result


def log_best(model, metric):
    logging.debug(model.best_iteration)
    logging.debug(model.best_score['valid_1'][metric])


def log_diff_best(model, metric):
    logging.debug(model.best_iteration)
    logging.debug(model.best_score['valid_1']['rmse'])


def cb_log_best(model, metric):
    logging.debug(model.best_iteration_)
    logging.debug(model.best_score_['validation_0'][metric])


def log_evaluation(logger, period=1, show_stdv=True, level=logging.DEBUG):
    def _callback(env):
        if period > 0 and env.evaluation_result_list \
                and (env.iteration + 1) % period == 0:
            result = '\t'.join([
                _format_eval_result(x, show_stdv)
                for x in env.evaluation_result_list
            ])
            logger.log(level, '[{}]\t{}'.format(env.iteration + 1, result))
    _callback.order = 10
    return _callback
