import db_connect as db

nzx_price_dict = {
    "2017-12-01": 1.105,
    "2017-12-04": 1.085268,
    "2017-12-05": 1.085268,
    "2017-12-06": 1.075402,
    "2017-12-07": 1.075402,
    "2017-12-08": 1.105,
    "2017-12-11": 1.095134,
    "2017-12-12": 1.085268,
    "2017-12-13": 1.105,
    "2017-12-14": 1.075402,
    "2017-12-15": 1.095134,
    "2017-12-18": 1.085268,
    "2017-12-19": 1.085268,
    "2017-12-20": 1.095134,
    "2017-12-21": 1.095134,
    "2017-12-27": 1.085268,
    "2017-12-28": 1.095134,
    "2017-12-29": 1.105,
    "2018-01-03": 1.114866,
    "2018-01-04": 1.105,
    "2018-01-05": 1.114866,
    "2018-01-08": 1.114866,
    "2018-01-09": 1.134598,
    "2018-01-10": 1.124732,
    "2018-01-11": 1.124732,
    "2018-01-12": 1.114866,
    "2018-01-15": 1.114866,
    "2018-01-16": 1.105,
    "2018-01-17": 1.124732,
    "2018-01-18": 1.114866,
    "2018-01-19": 1.124732,
    "2018-01-22": 1.105,
    "2018-01-23": 1.114866,
    "2018-01-24": 1.105,
    "2018-01-25": 1.114866,
    "2018-01-26": 1.105,
    "2018-01-29": 1.114866,
    "2018-01-30": 1.114866,
    "2018-01-31": 1.114866,
    "2018-02-01": 1.114866,
    "2018-02-02": 1.105,
    "2018-02-05": 1.085268,
    "2018-02-07": 1.105,
    "2018-02-08": 1.095134,
    "2018-02-09": 1.085268,
    "2018-02-12": 1.114866,
    "2018-02-13": 1.105,
    "2018-02-14": 1.095134,
    "2018-02-15": 1.095134,
    "2018-02-16": 1.095134,
    "2018-02-19": 1.085268,
    "2018-02-20": 1.095134,
    "2018-02-21": 1.065536,
    "2018-02-22": 1.065536,
    "2018-02-23": 1.045803,
    "2018-02-26": 1.055669,
    "2018-02-27": 1.055669,
    "2018-02-28": 1.035937,
    "2018-03-01": 1.055669,
    "2018-03-02": 1.055669,
    "2018-03-05": 1.055669,
    "2018-03-06": 1.075402,
    "2018-03-07": 1.075402,
    "2018-03-08": 1.045803,
    "2018-03-09": 1.075402,
    "2018-03-12": 1.075402,
    "2018-03-13": 1.065536,
    "2018-03-14": 1.085268,
    "2018-03-15": 1.055669,
    "2018-03-16": 1.085268,
    "2018-03-19": 1.065536,
    "2018-03-20": 1.065536,
    "2018-03-21": 1.055669,
    "2018-03-22": 1.065536,
    "2018-03-23": 1.075402,
    "2018-03-26": 1.075402,
    "2018-03-27": 1.085268,
    "2018-03-28": 1.065536,
    "2018-03-29": 1.055669,
    "2018-04-03": 1.065536,
    "2018-04-04": 1.065536,
    "2018-04-05": 1.065536,
    "2018-04-06": 1.065536,
    "2018-04-09": 1.065536,
    "2018-04-10": 1.065536,
    "2018-04-11": 1.075402,
    "2018-04-12": 1.065536,
    "2018-04-13": 1.075402,
    "2018-04-16": 1.065536,
    "2018-04-17": 1.085268,
    "2018-04-18": 1.065536,
    "2018-04-19": 1.065536,
    "2018-04-20": 1.055669,
    "2018-04-23": 1.065536,
    "2018-04-24": 1.055669,
    "2018-04-26": 1.055669,
    "2018-04-27": 1.065536,
    "2018-04-30": 1.065536,
    "2018-05-01": 1.055669,
    "2018-05-02": 1.055669,
    "2018-05-03": 1.065536,
    "2018-05-04": 1.045803,
    "2018-05-07": 1.065536,
    "2018-05-08": 1.075402,
    "2018-05-09": 1.075402,
    "2018-05-10": 1.075402,
    "2018-05-11": 1.085268,
    "2018-05-14": 1.085268,
    "2018-05-15": 1.085268,
    "2018-05-16": 1.085268,
    "2018-05-17": 1.095134,
    "2018-05-18": 1.105,
    "2018-05-21": 1.105,
    "2018-05-22": 1.114866,
    "2018-05-23": 1.114866,
    "2018-05-24": 1.114866,
    "2018-05-25": 1.114866,
    "2018-05-28": 1.114866,
    "2018-05-29": 1.114866,
    "2018-05-30": 1.105,
    "2018-05-31": 1.105,
    "2018-06-01": 1.105,
    "2018-06-05": 1.114866,
    "2018-06-06": 1.105,
    "2018-06-07": 1.114866,
    "2018-06-08": 1.114866,
    "2018-06-11": 1.124732,
    "2018-06-12": 1.114866,
    "2018-06-13": 1.124732,
    "2018-06-14": 1.114866,
    "2018-06-15": 1.124732,
    "2018-06-18": 1.114866,
    "2018-06-19": 1.114866,
    "2018-06-20": 1.124732,
    "2018-06-21": 1.124732,
    "2018-06-22": 1.114866,
    "2018-06-25": 1.114866,
    "2018-06-26": 1.124732,
    "2018-06-27": 1.114866,
    "2018-06-28": 1.124732,
    "2018-06-29": 1.114866,
    "2018-07-02": 1.105,
    "2018-07-03": 1.114866,
    "2018-07-04": 1.105,
    "2018-07-05": 1.114866,
    "2018-07-06": 1.095134,
    "2018-07-09": 1.095134,
    "2018-07-10": 1.095134,
    "2018-07-11": 1.095134,
    "2018-07-12": 1.095134,
    "2018-07-13": 1.095134,
    "2018-07-16": 1.095134,
    "2018-07-17": 1.105,
    "2018-07-18": 1.085268,
    "2018-07-19": 1.095134,
    "2018-07-20": 1.095134,
    "2018-07-23": 1.105,
    "2018-07-24": 1.095134,
    "2018-07-25": 1.095134,
    "2018-07-26": 1.085268,
    "2018-07-27": 1.095134,
    "2018-07-30": 1.085268,
    "2018-07-31": 1.085268,
    "2018-08-01": 1.075402,
    "2018-08-02": 1.075402,
    "2018-08-03": 1.075402,
    "2018-08-06": 1.065536,
    "2018-08-07": 1.075402,
    "2018-08-08": 1.065536,
    "2018-08-09": 1.065536,
    "2018-08-10": 1.085268,
    "2018-08-13": 1.075402,
    "2018-08-14": 1.075402,
    "2018-08-15": 1.095134,
    "2018-08-16": 1.085268,
    "2018-08-17": 1.085268,
    "2018-08-20": 1.085268,
    "2018-08-21": 1.105,
    "2018-08-22": 1.095134,
    "2018-08-23": 1.075402,
    "2018-08-24": 1.095134,
    "2018-08-27": 1.105,
    "2018-08-29": 1.105,
    "2018-08-30": 1.07,
    "2018-08-31": 1.05,
    "2018-09-03": 1.06,
    "2018-09-04": 1.06,
    "2018-09-05": 1.06,
    "2018-09-06": 1.06,
    "2018-09-07": 1.07,
    "2018-09-10": 1.07,
    "2018-09-11": 1.07,
    "2018-09-12": 1.08,
    "2018-09-13": 1.08,
    "2018-09-14": 1.11,
    "2018-09-17": 1.09,
    "2018-09-18": 1.11,
    "2018-09-19": 1.11,
    "2018-09-20": 1.1,
    "2018-09-21": 1.09,
    "2018-09-24": 1.09,
    "2018-09-25": 1.1,
    "2018-09-26": 1.08,
    "2018-09-27": 1.1,
    "2018-09-28": 1.1,
    "2018-10-01": 1.08,
    "2018-10-02": 1.09,
    "2018-10-03": 1.08,
    "2018-10-04": 1.08,
    "2018-10-05": 1.08,
    "2018-10-08": 1.09,
    "2018-10-09": 1.08,
    "2018-10-10": 1.11,
    "2018-10-11": 1.07,
    "2018-10-12": 1.05,
    "2018-10-15": 1.05,
    "2018-10-16": 1.03,
    "2018-10-17": 1.05,
    "2018-10-18": 1.07,
    "2018-10-19": 1.05,
    "2018-10-23": 1.07,
    "2018-10-24": 1.06,
    "2018-10-25": 1.04,
    "2018-10-26": 1.03,
    "2018-10-29": 1.03,
    "2018-10-30": 1.06,
    "2018-10-31": 1.05,
    "2018-11-01": 1.07,
    "2018-11-02": 1.07,
    "2018-11-05": 1.07,
    "2018-11-06": 1.06,
    "2018-11-07": 1.05,
    "2018-11-08": 1.05,
    "2018-11-09": 1.04,
    "2018-11-12": 1.04,
    "2018-11-13": 1.04,
    "2018-11-14": 1.03,
    "2018-11-15": 1.02,
    "2018-11-16": 1.04,
    "2018-11-19": 1.03,
    "2018-11-20": 1.04,
    "2018-11-21": 1.03,
    "2018-11-22": 1.02,
    "2018-11-23": 1.02,
    "2018-11-26": 1.02,
    "2018-11-27": 1.03,
    "2018-11-28": 1.03,
    "2018-11-29": 1.02,
    "2018-11-30": 1.04,
    "2018-12-03": 1.03,
    "2018-12-04": 1.02,
    "2018-12-05": 1.02,
    "2018-12-06": 1.02,
    "2018-12-07": 1.03,
    "2018-12-10": 1.02,
    "2018-12-11": 1.02,
    "2018-12-12": 1,
    "2018-12-13": 1,
    "2018-12-14": 1,
    "2018-12-17": 1.02,
    "2018-12-18": 0.98,
    "2018-12-19": 0.99,
    "2018-12-20": 0.98,
    "2018-12-21": 0.98,
    "2018-12-24": 1,
    "2018-12-27": 0.98,
    "2018-12-28": 1,
    "2018-12-31": 1.01,
    "2019-01-03": 0.98,
    "2019-01-04": 0.99,
    "2019-01-07": 0.99,
    "2019-01-08": 0.98,
    "2019-01-09": 0.99,
    "2019-01-10": 1,
    "2019-01-11": 0.99,
    "2019-01-14": 0.98,
    "2019-01-15": 0.98,
    "2019-01-16": 0.98,
    "2019-01-17": 0.99,
    "2019-01-18": 0.99,
    "2019-01-21": 0.99,
    "2019-01-22": 1,
    "2019-01-23": 0.98,
    "2019-01-24": 0.99,
    "2019-01-25": 0.99,
    "2019-01-28": 0.98,
    "2019-01-29": 0.98,
    "2019-01-30": 0.99,
    "2019-01-31": 1,
    "2019-02-01": 1.02,
    "2019-02-04": 1.02,
    "2019-02-05": 1.02,
    "2019-02-07": 0.99,
    "2019-02-08": 0.97,
    "2019-02-11": 0.97,
    "2019-02-12": 0.99,
    "2019-02-13": 1.01,
    "2019-02-14": 1.02,
    "2019-02-15": 1.02,
    "2019-02-18": 1.01,
    "2019-02-19": 1.02,
    "2019-02-20": 1.01,
    "2019-02-21": 1.01,
    "2019-02-22": 1.01,
    "2019-02-25": 1.03,
    "2019-02-26": 1,
    "2019-02-27": 1.01,
    "2019-02-28": 1.01,
    "2019-03-01": 1.02,
    "2019-03-04": 1,
    "2019-03-05": 1.02,
    "2019-03-06": 1.02,
    "2019-03-07": 0.98,
    "2019-03-08": 1,
    "2019-03-11": 0.98,
    "2019-03-12": 1,
    "2019-03-13": 0.99,
    "2019-03-14": 0.99,
    "2019-03-15": 1.01,
    "2019-03-18": 0.99,
    "2019-03-19": 0.99,
    "2019-03-20": 0.99,
    "2019-03-21": 1,
    "2019-03-22": 0.99,
    "2019-03-25": 0.99,
    "2019-03-26": 1,
    "2019-03-27": 1,
    "2019-03-28": 0.99,
    "2019-03-29": 1,
    "2019-04-01": 1,
    "2019-04-02": 1.01,
    "2019-04-03": 1,
    "2019-04-04": 1.01,
    "2019-04-05": 1.01,
    "2019-04-08": 1.01,
    "2019-04-09": 1.02,
    "2019-04-10": 1.01,
    "2019-04-11": 1,
    "2019-04-12": 1,
    "2019-04-15": 1,
    "2019-04-16": 1,
    "2019-04-17": 1,
    "2019-04-18": 1.01,
    "2019-04-23": 1,
    "2019-04-24": 1.01,
    "2019-04-26": 1.01,
    "2019-04-29": 1,
    "2019-04-30": 1.01,
    "2019-05-01": 1.02,
    "2019-05-02": 1.07,
    "2019-05-03": 1.04,
    "2019-05-06": 1.05,
    "2019-05-07": 1.07,
    "2019-05-08": 1.08,
    "2019-05-09": 1.08,
    "2019-05-10": 1.06,
    "2019-05-13": 1.06,
    "2019-05-14": 1.06,
    "2019-05-15": 1.06,
    "2019-05-16": 1.07,
    "2019-05-17": 1.09,
    "2019-05-20": 1.07,
    "2019-05-21": 1.05,
    "2019-05-22": 1.07,
    "2019-05-23": 1.07,
    "2019-05-24": 1.07,
    "2019-05-27": 1.07,
    "2019-05-28": 1.05,
    "2019-05-29": 1.05,
    "2019-05-30": 1.05,
    "2019-05-31": 1.05,
    "2019-06-04": 1.05,
    "2019-06-05": 1.05,
    "2019-06-06": 1.05,
    "2019-06-07": 1.05,
    "2019-06-10": 1.07,
    "2019-06-11": 1.06,
    "2019-06-12": 1.07,
    "2019-06-13": 1.09,
    "2019-06-14": 1.09,
    "2019-06-17": 1.09,
    "2019-06-18": 1.09,
    "2019-06-19": 1.09,
    "2019-06-20": 1.08,
    "2019-06-21": 1.08,
    "2019-06-24": 1.1,
    "2019-06-25": 1.1,
    "2019-06-26": 1.1,
    "2019-06-27": 1.12,
    "2019-06-28": 1.12,
    "2019-07-01": 1.12,
    "2019-07-02": 1.12,
    "2019-07-03": 1.12,
    "2019-07-04": 1.12,
    "2019-07-05": 1.12,
    "2019-07-08": 1.12,
    "2019-07-09": 1.12,
    "2019-07-10": 1.15,
    "2019-07-11": 1.13,
    "2019-07-12": 1.15,
    "2019-07-15": 1.17,
    "2019-07-16": 1.17,
    "2019-07-17": 1.17,
    "2019-07-18": 1.18,
    "2019-07-19": 1.2,
    "2019-07-22": 1.2,
    "2019-07-23": 1.2,
    "2019-07-24": 1.18,
    "2019-07-25": 1.2,
    "2019-07-26": 1.2,
    "2019-07-29": 1.18,
    "2019-07-30": 1.18,
    "2019-07-31": 1.19,
    "2019-08-01": 1.18,
    "2019-08-02": 1.19,
    "2019-08-05": 1.18,
    "2019-08-06": 1.17,
    "2019-08-07": 1.19,
    "2019-08-08": 1.19,
    "2019-08-09": 1.19,
    "2019-08-12": 1.2,
    "2019-08-13": 1.2,
    "2019-08-14": 1.23,
    "2019-08-15": 1.2,
    "2019-08-16": 1.22,
    "2019-08-19": 1.2,
    "2019-08-20": 1.22,
    "2019-08-21": 1.24,
    "2019-08-22": 1.25,
    "2019-08-23": 1.24,
    "2019-08-26": 1.25,
    "2019-08-27": 1.26,
    "2019-08-28": 1.28,
    "2019-08-29": 1.26,
    "2019-08-30": 1.26,
    "2019-09-02": 1.27,
    "2019-09-03": 1.27,
    "2019-09-04": 1.27,
    "2019-09-05": 1.27,
    "2019-09-06": 1.29,
    "2019-09-09": 1.28,
    "2019-09-10": 1.29,
    "2019-09-11": 1.29,
    "2019-09-12": 1.28,
    "2019-09-13": 1.25,
    "2019-09-16": 1.25,
    "2019-09-17": 1.26,
    "2019-09-18": 1.26,
    "2019-09-19": 1.28,
    "2019-09-20": 1.28,
    "2019-09-23": 1.27,
    "2019-09-24": 1.27,
    "2019-09-25": 1.26,
    "2019-09-26": 1.27,
    "2019-09-27": 1.28,
    "2019-09-30": 1.29,
    "2019-10-01": 1.28,
    "2019-10-02": 1.27,
    "2019-10-03": 1.26,
    "2019-10-04": 1.25,
    "2019-10-07": 1.25,
    "2019-10-08": 1.27,
    "2019-10-09": 1.28,
    "2019-10-10": 1.27,
    "2019-10-11": 1.28,
    "2019-10-14": 1.27,
    "2019-10-15": 1.28,
    "2019-10-16": 1.28,
    "2019-10-17": 1.29,
    "2019-10-18": 1.29,
    "2019-10-21": 1.28,
    "2019-10-22": 1.28,
    "2019-10-23": 1.27,
    "2019-10-24": 1.27,
    "2019-10-25": 1.27,
    "2019-10-29": 1.22,
    "2019-10-30": 1.27,
    "2019-10-31": 1.29,
    "2019-11-01": 1.28,
    "2019-11-04": 1.26,
    "2019-11-05": 1.26,
    "2019-11-06": 1.28,
    "2019-11-07": 1.3,
    "2019-11-08": 1.29,
    "2019-11-11": 1.25,
    "2019-11-12": 1.28,
    "2019-11-13": 1.25,
    "2019-11-14": 1.25,
    "2019-11-15": 1.25,
    "2019-11-18": 1.23,
    "2019-11-19": 1.24,
    "2019-11-20": 1.26,
    "2019-11-21": 1.24,
    "2019-11-22": 1.24,
    "2019-11-25": 1.23,
    "2019-11-26": 1.24,
    "2019-11-27": 1.24,
    "2019-11-28": 1.24,
    "2019-11-29": 1.22,
    "2019-12-02": 1.24,
    "2019-12-03": 1.24,
    "2019-12-04": 1.22,
    "2019-12-05": 1.24,
    "2019-12-06": 1.23,
    "2019-12-09": 1.28,
    "2019-12-10": 1.28,
    "2019-12-11": 1.28,
    "2019-12-12": 1.29,
    "2019-12-13": 1.28,
    "2019-12-16": 1.28,
    "2019-12-17": 1.29,
    "2019-12-18": 1.32,
    "2019-12-19": 1.33,
    "2019-12-20": 1.33,
    "2019-12-23": 1.33,
    "2019-12-24": 1.3,
    "2019-12-27": 1.34,
    "2019-12-30": 1.34,
    "2019-12-31": 1.36,
    "2020-01-03": 1.35,
    "2020-01-06": 1.34,
    "2020-01-07": 1.35,
    "2020-01-08": 1.32,
    "2020-01-09": 1.34,
    "2020-01-10": 1.37,
    "2020-01-13": 1.34,
    "2020-01-14": 1.37,
    "2020-01-15": 1.37,
    "2020-01-16": 1.37,
    "2020-01-17": 1.37,
    "2020-01-20": 1.38,
    "2020-01-21": 1.35,
    "2020-01-22": 1.37,
    "2020-01-23": 1.39,
    "2020-01-24": 1.39,
    "2020-01-27": 1.39,
    "2020-01-28": 1.37,
    "2020-01-29": 1.37,
    "2020-01-30": 1.39,
    "2020-01-31": 1.39,
    "2020-02-03": 1.37,
    "2020-02-04": 1.33,
    "2020-02-05": 1.35,
    "2020-02-07": 1.37,
    "2020-02-10": 1.37,
    "2020-02-11": 1.39,
    "2020-02-12": 1.38,
    "2020-02-13": 1.43,
    "2020-02-14": 1.45,
    "2020-02-17": 1.45,
    "2020-02-18": 1.47,
    "2020-02-19": 1.48,
    "2020-02-20": 1.46,
    "2020-02-21": 1.45,
    "2020-02-24": 1.41,
    "2020-02-25": 1.4,
    "2020-02-26": 1.33,
    "2020-02-27": 1.33,
    "2020-02-28": 1.33,
    "2020-03-02": 1.3,
    "2020-03-03": 1.35,
    "2020-03-04": 1.35,
    "2020-03-05": 1.34,
    "2020-03-06": 1.3,
    "2020-03-09": 1.25,
    "2020-03-10": 1.22,
    "2020-03-11": 1.23,
    "2020-03-12": 1.2,
    "2020-03-13": 1.14,
    "2020-03-16": 1.08,
    "2020-03-17": 1.03,
    "2020-03-18": 1.07,
    "2020-03-19": 1.04,
    "2020-03-20": 1.04,
    "2020-03-23": 0.95,
    "2020-03-24": 0.95,
    "2020-03-25": 1,
    "2020-03-26": 1.07,
    "2020-03-27": 1.05,
    "2020-03-30": 1.09,
    "2020-03-31": 1.11,
    "2020-04-01": 1.1,
    "2020-04-02": 1.1,
    "2020-04-03": 1.09,
    "2020-04-06": 1.08,
    "2020-04-07": 1.16,
    "2020-04-08": 1.17,
    "2020-04-09": 1.19,
    "2020-04-14": 1.25,
    "2020-04-15": 1.26,
    "2020-04-16": 1.33,
    "2020-04-17": 1.37,
    "2020-04-20": 1.27,
    "2020-04-21": 1.28,
    "2020-04-22": 1.27,
    "2020-04-23": 1.26,
    "2020-04-24": 1.25,
    "2020-04-28": 1.25,
    "2020-04-29": 1.26,
    "2020-04-30": 1.28,
    "2020-05-01": 1.27,
    "2020-05-04": 1.26,
    "2020-05-05": 1.27,
    "2020-05-06": 1.29,
    "2020-05-07": 1.29,
    "2020-05-08": 1.28,
    "2020-05-11": 1.28,
    "2020-05-12": 1.3,
    "2020-05-13": 1.35,
    "2020-05-14": 1.38,
    "2020-05-15": 1.4,
    "2020-05-18": 1.35,
    "2020-05-19": 1.37,
    "2020-05-20": 1.38,
    "2020-05-21": 1.4,
    "2020-05-22": 1.39,
    "2020-05-25": 1.38,
    "2020-05-26": 1.41,
    "2020-05-27": 1.42,
    "2020-05-28": 1.4,
    "2020-05-29": 1.42,
    "2020-06-02": 1.42,
    "2020-06-03": 1.41,
    "2020-06-04": 1.43,
    "2020-06-05": 1.45,
    "2020-06-08": 1.48,
    "2020-06-09": 1.46,
    "2020-06-10": 1.44,
    "2020-06-11": 1.42,
    "2020-06-12": 1.41,
    "2020-06-15": 1.38,
    "2020-06-16": 1.38,
    "2020-06-17": 1.4,
    "2020-06-18": 1.39,
    "2020-06-19": 1.44,
    "2020-06-22": 1.43,
    "2020-06-23": 1.41,
    "2020-06-24": 1.43,
    "2020-06-25": 1.42,
    "2020-06-26": 1.39,
    "2020-06-29": 1.39,
    "2020-06-30": 1.4,
    "2020-07-01": 1.41,
    "2020-07-02": 1.42,
    "2020-07-03": 1.42,
    "2020-07-06": 1.42,
    "2020-07-07": 1.42,
    "2020-07-08": 1.42,
    "2020-07-09": 1.41,
    "2020-07-10": 1.43,
    "2020-07-13": 1.42,
    "2020-07-14": 1.43,
    "2020-07-15": 1.41,
    "2020-07-16": 1.41,
    "2020-07-17": 1.44,
    "2020-07-20": 1.43,
    "2020-07-21": 1.44,
    "2020-07-22": 1.44,
    "2020-07-23": 1.44,
    "2020-07-24": 1.44,
    "2020-07-27": 1.46,
    "2020-07-28": 1.45,
    "2020-07-29": 1.45,
    "2020-07-30": 1.45,
    "2020-07-31": 1.46,
    "2020-08-03": 1.45,
    "2020-08-04": 1.47,
    "2020-08-05": 1.47,
    "2020-08-06": 1.5,
    "2020-08-07": 1.49,
    "2020-08-10": 1.53,
    "2020-08-11": 1.54,
    "2020-08-12": 1.53,
    "2020-08-13": 1.57,
    "2020-08-14": 1.54,
    "2020-08-17": 1.6,
    "2020-08-18": 1.62,
    "2020-08-19": 1.63,
    "2020-08-20": 1.65,
    "2020-08-21": 1.65,
    "2020-08-24": 1.66,
    "2020-08-25": 1.68,
    "2020-08-26": 1.68,
    "2020-08-27": 1.69,
    "2020-08-28": 1.64,
    "2020-08-31": 1.62,
    "2020-09-01": 1.62,
    "2020-09-02": 1.65,
    "2020-09-03": 1.65,
    "2020-09-04": 1.63,
    "2020-09-07": 1.63,
    "2020-09-08": 1.62,
    "2020-09-09": 1.58,
    "2020-09-10": 1.6,
    "2020-09-11": 1.6,
    "2020-09-14": 1.64,
    "2020-09-15": 1.62,
    "2020-09-16": 1.61,
    "2020-09-17": 1.61,
    "2020-09-18": 1.58,
    "2020-09-21": 1.58,
    "2020-09-22": 1.6,
    "2020-09-23": 1.61,
    "2020-09-24": 1.6,
    "2020-09-25": 1.62,
    "2020-09-28": 1.62,
    "2020-09-29": 1.64,
    "2020-09-30": 1.62,
    "2020-10-01": 1.63,
    "2020-10-02": 1.59,
    "2020-10-05": 1.61,
    "2020-10-06": 1.6,
    "2020-10-07": 1.62,
    "2020-10-08": 1.62,
    "2020-10-09": 1.65,
    "2020-10-12": 1.67,
    "2020-10-13": 1.68,
    "2020-10-14": 1.68,
    "2020-10-15": 1.68,
    "2020-10-16": 1.7,
    "2020-10-19": 1.72,
    "2020-10-20": 1.75,
    "2020-10-21": 1.72,
    "2020-10-22": 1.77,
    "2020-10-23": 1.74,
    "2020-10-27": 1.75,
    "2020-10-28": 1.75,
    "2020-10-29": 1.73,
    "2020-10-30": 1.72,
    "2020-11-02": 1.72,
    "2020-11-03": 1.72,
    "2020-11-04": 1.72,
    "2020-11-05": 1.73,
    "2020-11-06": 1.78,
    "2020-11-09": 1.82,
    "2020-11-10": 1.85,
    "2020-11-11": 1.75,
    "2020-11-12": 1.84,
    "2020-11-13": 1.8,
    "2020-11-16": 1.8,
    "2020-11-17": 1.83,
    "2020-11-18": 1.81,
    "2020-11-19": 1.81,
    "2020-11-20": 1.82,
    "2020-11-23": 1.84,
    "2020-11-24": 1.82,
    "2020-11-25": 1.84,
    "2020-11-26": 1.85,
    "2020-11-27": 1.86,
    "2020-11-30": 1.83,
    "2020-12-01": 1.85,
    "2020-12-02": 1.84,
    "2020-12-03": 1.84,
    "2020-12-04": 1.86,
    "2020-12-07": 1.88,
    "2020-12-08": 1.87,
    "2020-12-09": 1.87,
    "2020-12-10": 1.85,
    "2020-12-11": 1.86,
    "2020-12-14": 1.91,
    "2020-12-15": 1.9,
    "2020-12-16": 1.9,
    "2020-12-17": 1.94,
    "2020-12-18": 1.96,
    "2020-12-21": 1.98,
    "2020-12-22": 1.97,
    "2020-12-23": 1.96,
    "2020-12-24": 1.96,
    "2020-12-29": 1.95,
    "2020-12-30": 1.95,
    "2020-12-31": 1.96,
    "2021-01-05": 1.96,
    "2021-01-06": 1.96,
    "2021-01-07": 1.96,
    "2021-01-08": 2,
    "2021-01-11": 2,
    "2021-01-12": 2.02,
    "2021-01-13": 2.09,
    "2021-01-14": 2.16,
    "2021-01-15": 2.15,
    "2021-01-18": 2.1,
    "2021-01-19": 2.1,
    "2021-01-20": 2.1,
    "2021-01-21": 2.13,
    "2021-01-22": 2.13,
    "2021-01-25": 2.15,
    "2021-01-26": 2.13,
    "2021-01-27": 2.12,
    "2021-01-28": 2.04,
    "2021-01-29": 2.05,
    "2021-02-01": 2.05,
    "2021-02-02": 2.03,
    "2021-02-03": 2.04,
    "2021-02-04": 2,
    "2021-02-05": 2.02,
    "2021-02-09": 2.03,
    "2021-02-10": 2.03,
    "2021-02-11": 2,
    "2021-02-12": 2.03,
    "2021-02-15": 2,
    "2021-02-16": 1.99,
    "2021-02-17": 2,
    "2021-02-18": 2.02,
    "2021-02-19": 2.02,
    "2021-02-22": 2.01,
    "2021-02-23": 2.01,
    "2021-02-24": 2.01,
    "2021-02-25": 1.9,
    "2021-02-26": 1.93,
    "2021-03-01": 2,
    "2021-03-02": 2.02,
    "2021-03-03": 2,
    "2021-03-04": 1.98,
    "2021-03-05": 1.96,
    "2021-03-08": 1.98,
    "2021-03-09": 1.91,
    "2021-03-10": 1.92,
    "2021-03-11": 1.9,
    "2021-03-12": 1.93,
    "2021-03-15": 1.96,
    "2021-03-16": 1.99,
    "2021-03-17": 2,
    "2021-03-18": 2,
    "2021-03-19": 2.02,
    "2021-03-22": 1.98,
    "2021-03-23": 1.96,
    "2021-03-24": 1.98,
    "2021-03-25": 2.03,
    "2021-03-26": 2.03,
    "2021-03-29": 2.02,
    "2021-03-30": 2.02,
    "2021-03-31": 2.1,
    "2021-04-01": 2.1,
    "2021-04-06": 2.09,
    "2021-04-07": 2.06,
    "2021-04-08": 2.09,
    "2021-04-09": 2.08,
    "2021-04-12": 2.08,
    "2021-04-13": 2.08,
    "2021-04-14": 2.09,
    "2021-04-15": 2.1,
    "2021-04-16": 2.09,
    "2021-04-19": 2.07,
    "2021-04-20": 2.06,
    "2021-04-21": 2.06,
    "2021-04-22": 2.08,
    "2021-04-23": 2.05,
    "2021-04-27": 2.1,
    "2021-04-28": 2.07,
    "2021-04-29": 2.07,
    "2021-04-30": 2.07,
    "2021-05-03": 2.05,
    "2021-05-04": 2.05,
    "2021-05-05": 2.05,
    "2021-05-06": 2.02,
    "2021-05-07": 2,
    "2021-05-10": 2.03,
    "2021-05-11": 1.99,
    "2021-05-12": 2.01,
    "2021-05-13": 2.04,
    "2021-05-14": 1.99,
    "2021-05-17": 2.05,
    "2021-05-18": 2.06,
    "2021-05-19": 2.04,
    "2021-05-20": 2.01,
    "2021-05-21": 2.02,
    "2021-05-24": 2.01,
    "2021-05-25": 2.03,
    "2021-05-26": 2.06,
    "2021-05-27": 2.09,
    "2021-05-28": 2.06,
    "2021-05-31": 2.12,
    "2021-06-01": 2.07,
    "2021-06-02": 2.13,
    "2021-06-03": 2.08,
    "2021-06-04": 2.1,
    "2021-06-08": 2.06,
    "2021-06-09": 2.05,
    "2021-06-10": 2.1,
    "2021-06-11": 2.07,
    "2021-06-14": 2.09,
    "2021-06-15": 2.07,
    "2021-06-16": 2.07,
    "2021-06-17": 2.08,
    "2021-06-18": 2.07,
    "2021-06-21": 2.06,
    "2021-06-22": 2.06,
    "2021-06-23": 2.05,
    "2021-06-24": 2.05,
    "2021-06-25": 2.04,
    "2021-06-28": 2,
    "2021-06-29": 2,
    "2021-06-30": 2,
    "2021-07-01": 1.99,
    "2021-07-02": 1.98,
    "2021-07-05": 1.99,
    "2021-07-06": 2.02,
    "2021-07-07": 2,
    "2021-07-08": 1.98,
    "2021-07-09": 2,
    "2021-07-12": 1.97,
    "2021-07-13": 1.97,
    "2021-07-14": 1.93,
    "2021-07-15": 1.93,
    "2021-07-16": 1.92,
    "2021-07-19": 1.88,
    "2021-07-20": 1.82,
    "2021-07-21": 1.91,
    "2021-07-22": 1.9,
    "2021-07-23": 1.91,
    "2021-07-26": 1.88,
    "2021-07-27": 1.91,
    "2021-07-28": 1.94,
    "2021-07-29": 1.92,
    "2021-07-30": 1.92,
    "2021-08-02": 1.86,
    "2021-08-03": 1.85,
    "2021-08-04": 1.86,
    "2021-08-05": 1.84,
    "2021-08-06": 1.89,
    "2021-08-09": 1.89,
    "2021-08-10": 1.86,
    "2021-08-11": 1.86,
    "2021-08-12": 1.86,
    "2021-08-13": 1.87,
    "2021-08-16": 1.86,
    "2021-08-17": 1.8,
    "2021-08-18": 1.85,
    "2021-08-19": 1.85,
    "2021-08-20": 1.87,
    "2021-08-23": 1.85,
    "2021-08-24": 1.88,
    "2021-08-25": 1.9,
    "2021-08-26": 1.86,
    "2021-08-27": 1.82,
    "2021-08-30": 1.81,
    "2021-08-31": 1.84,
    "2021-09-01": 1.84,
    "2021-09-02": 1.83,
    "2021-09-03": 1.85,
    "2021-09-06": 1.82,
    "2021-09-07": 1.81,
    "2021-09-08": 1.8,
    "2021-09-09": 1.75,
    "2021-09-10": 1.72,
    "2021-09-13": 1.7,
    "2021-09-14": 1.71,
    "2021-09-15": 1.75,
    "2021-09-16": 1.71,
    "2021-09-17": 1.75,
    "2021-09-20": 1.73,
    "2021-09-21": 1.73,
    "2021-09-22": 1.74,
    "2021-09-23": 1.73,
    "2021-09-24": 1.75,
    "2021-09-27": 1.73,
    "2021-09-28": 1.7,
    "2021-09-29": 1.69,
    "2021-09-30": 1.7,
    "2021-10-01": 1.73,
    "2021-10-04": 1.73,
    "2021-10-05": 1.73,
    "2021-10-06": 1.73,
    "2021-10-07": 1.72,
    "2021-10-08": 1.72,
    "2021-10-11": 1.71,
    "2021-10-12": 1.7,
    "2021-10-13": 1.7,
    "2021-10-14": 1.7,
    "2021-10-15": 1.73,
    "2021-10-18": 1.75,
    "2021-10-19": 1.74,
    "2021-10-20": 1.72,
    "2021-10-21": 1.74,
    "2021-10-22": 1.75,
    "2021-10-26": 1.73,
    "2021-10-27": 1.71,
    "2021-10-28": 1.71,
    "2021-10-29": 1.73,
    "2021-11-01": 1.76,
    "2021-11-02": 1.76,
    "2021-11-03": 1.74,
    "2021-11-04": 1.76,
    "2021-11-05": 1.77,
    "2021-11-08": 1.75,
    "2021-11-09": 1.77,
    "2021-11-10": 1.76,
    "2021-11-11": 1.76,
    "2021-11-12": 1.78,
    "2021-11-15": 1.8,
    "2021-11-16": 1.8,
    "2021-11-17": 1.75,
    "2021-11-18": 1.74,
    "2021-11-19": 1.76,
    "2021-11-22": 1.76,
    "2021-11-23": 1.75,
    "2021-11-24": 1.77,
    "2021-11-25": 1.76,
    "2021-11-26": 1.77,
    "2021-11-29": 1.74,
    "2021-11-30": 1.75,
    "2021-12-01": 1.8,
    "2021-12-02": 1.75,
    "2021-12-03": 1.77,
    "2021-12-06": 1.76,
    "2021-12-07": 1.75,
    "2021-12-08": 1.8,
    "2021-12-09": 1.79,
    "2021-12-10": 1.79,
    "2021-12-13": 1.79,
    "2021-12-14": 1.78,
    "2021-12-15": 1.77,
    "2021-12-16": 1.79,
    "2021-12-17": 1.79,
    "2021-12-20": 1.79,
    "2021-12-21": 1.8,
    "2021-12-22": 1.85,
    "2021-12-23": 1.81,
    "2021-12-24": 1.8,
    "2021-12-29": 1.79,
    "2021-12-30": 1.83,
    "2021-12-31": 1.81,
    "2022-01-05": 1.83,
    "2022-01-06": 1.81,
    "2022-01-07": 1.81,
    "2022-01-10": 1.8,
    "2022-01-11": 1.8,
    "2022-01-12": 1.81,
    "2022-01-13": 1.79,
    "2022-01-14": 1.81,
    "2022-01-17": 1.82,
    "2022-01-18": 1.82,
    "2022-01-19": 1.76,
    "2022-01-20": 1.75,
    "2022-01-21": 1.76,
    "2022-01-24": 1.72,
    "2022-01-25": 1.72,
    "2022-01-26": 1.77,
    "2022-01-27": 1.73,
    "2022-01-28": 1.74,
    "2022-01-31": 1.76,
    "2022-02-01": 1.76,
    "2022-02-02": 1.73,
    "2022-02-03": 1.74,
    "2022-02-04": 1.73,
    "2022-02-08": 1.75,
    "2022-02-09": 1.74,
    "2022-02-10": 1.76,
    "2022-02-11": 1.76,
    "2022-02-14": 1.74,
    "2022-02-15": 1.72,
    "2022-02-16": 1.69900013,
    "2022-02-21": 1.62,
    "2022-02-22": 1.56,
    "2022-02-23": 1.52,
    "2022-02-24": 1.45,
    "2022-02-25": 1.45,
    "2022-02-28": 1.41,
    "2022-03-01": 1.43,
    "2022-03-02": 1.42,
    "2022-03-03": 1.43,
    "2022-03-04": 1.44,
    "2022-03-07": 1.41,
    "2022-03-08": 1.38,
    "2022-03-09": 1.38,
    "2022-03-10": 1.39,
    "2022-03-11": 1.39,
    "2022-03-14": 1.38,
    "2022-03-16": 1.38,
    "2022-03-17": 1.37,
    "2022-03-18": 1.4,
    "2022-03-21": 1.42,
    "2022-03-22": 1.42,
    "2022-03-23": 1.44,
    "2022-03-24": 1.44,
    "2022-03-25": 1.43,
    "2022-03-28": 1.43,
    "2022-03-29": 1.44,
    "2022-03-30": 1.44,
    "2022-03-31": 1.43,
    "2022-04-01": 1.43,
    "2022-04-04": 1.42,
    "2022-04-05": 1.42,
    "2022-04-06": 1.42,
    "2022-04-07": 1.4,
    "2022-04-08": 1.38,
    "2022-04-11": 1.38,
    "2022-04-12": 1.37,
    "2022-04-13": 1.4,
    "2022-04-14": 1.38,
    "2022-04-19": 1.35,
    "2022-04-20": 1.33,
    "2022-04-21": 1.33,
    "2022-04-22": 1.31,
    "2022-04-26": 1.3,
    "2022-04-27": 1.27,
    "2022-04-28": 1.29,
    "2022-04-29": 1.28,
    "2022-05-02": 1.27,
    "2022-05-03": 1.28,
    "2022-05-04": 1.26,
    "2022-05-05": 1.27,
    "2022-05-06": 1.25,
    "2022-05-09": 1.27,
    "2022-05-10": 1.26,
    "2022-05-11": 1.26,
    "2022-05-12": 1.29,
    "2022-05-13": 1.29,
    "2022-05-16": 1.28,
    "2022-05-17": 1.33,
    "2022-05-18": 1.32,
    "2022-05-19": 1.28,
    "2022-05-20": 1.3,
    "2022-05-23": 1.3,
    "2022-05-24": 1.3,
    "2022-05-25": 1.29,
    "2022-05-26": 1.28,
    "2022-05-27": 1.28,
    "2022-05-30": 1.28,
    "2022-05-31": 1.28,
    "2022-06-01": 1.28,
    "2022-06-02": 1.28,
    "2022-06-03": 1.26,
    "2022-06-07": 1.25,
    "2022-06-08": 1.21,
    "2022-06-09": 1.27,
    "2022-06-10": 1.28,
    "2022-06-13": 1.26,
    "2022-06-14": 1.27,
    "2022-06-15": 1.27,
    "2022-06-16": 1.26,
    "2022-06-17": 1.29,
    "2022-06-20": 1.27,
    "2022-06-21": 1.25,
    "2022-06-22": 1.26,
    "2022-06-23": 1.27,
    "2022-06-27": 1.27,
    "2022-06-28": 1.27,
    "2022-06-29": 1.25,
    "2022-06-30": 1.23,
    "2022-07-01": 1.23,
    "2022-07-04": 1.22,
    "2022-07-05": 1.2,
    "2022-07-06": 1.24,
    "2022-07-07": 1.26,
    "2022-07-08": 1.26,
    "2022-07-11": 1.25,
    "2022-07-12": 1.26,
    "2022-07-13": 1.26,
    "2022-07-14": 1.22,
    "2022-07-15": 1.24,
    "2022-07-18": 1.22,
    "2022-07-19": 1.25,
    "2022-07-20": 1.25,
    "2022-07-21": 1.24,
    "2022-07-22": 1.24,
    "2022-07-25": 1.23,
    "2022-07-26": 1.23,
    "2022-07-27": 1.21,
    "2022-07-28": 1.21,
    "2022-07-29": 1.2,
    "2022-08-01": 1.21,
    "2022-08-02": 1.21,
    "2022-08-03": 1.2,
    "2022-08-04": 1.21,
    "2022-08-05": 1.23,
    "2022-08-08": 1.24,
    "2022-08-09": 1.21,
    "2022-08-10": 1.25,
    "2022-08-11": 1.25,
    "2022-08-12": 1.25,
    "2022-08-15": 1.28,
    "2022-08-16": 1.28,
    "2022-08-17": 1.31,
    "2022-08-18": 1.31,
    "2022-08-19": 1.35,
    "2022-08-22": 1.36,
    "2022-08-23": 1.35,
    "2022-08-24": 1.33,
    "2022-08-25": 1.31,
    "2022-08-26": 1.31,
    "2022-08-29": 1.3,
    "2022-08-30": 1.3,
    "2022-08-31": 1.3,
    "2022-09-01": 1.29,
    "2022-09-02": 1.29,
    "2022-09-05": 1.29,
    "2022-09-06": 1.29,
    "2022-09-07": 1.27,
    "2022-09-08": 1.23,
    "2022-09-09": 1.25,
    "2022-09-12": 1.23,
    "2022-09-13": 1.21,
    "2022-09-14": 1.21,
    "2022-09-15": 1.25,
    "2022-09-16": 1.22,
    "2022-09-19": 1.23,
    "2022-09-20": 1.22,
    "2022-09-21": 1.22,
    "2022-09-22": 1.22,
    "2022-09-23": 1.23,
    "2022-09-27": 1.2,
    "2022-09-28": 1.21,
    "2022-09-29": 1.22,
    "2022-09-30": 1.2,
    "2022-10-03": 1.18,
    "2022-10-04": 1.19,
    "2022-10-05": 1.19,
    "2022-10-06": 1.21,
    "2022-10-07": 1.2,
    "2022-10-10": 1.18,
    "2022-10-11": 1.16,
    "2022-10-12": 1.19,
    "2022-10-13": 1.18,
    "2022-10-14": 1.2,
    "2022-10-17": 1.21,
    "2022-10-18": 1.2,
    "2022-10-19": 1.19,
    "2022-10-20": 1.19,
    "2022-10-21": 1.17,
    "2022-10-25": 1.17,
    "2022-10-26": 1.19,
    "2022-10-27": 1.2,
    "2022-10-28": 1.17,
    "2022-10-31": 1.2,
    "2022-11-01": 1.19,
    "2022-11-02": 1.19,
    "2022-11-03": 1.17,
    "2022-11-04": 1.17,
    "2022-11-07": 1.17,
    "2022-11-08": 1.18,
    "2022-11-09": 1.17,
    "2022-11-10": 1.18,
    "2022-11-11": 1.19,
    "2022-11-14": 1.18,
    "2022-11-15": 1.21,
    "2022-11-16": 1.24,
    "2022-11-17": 1.22,
    "2022-11-18": 1.22,
    "2022-11-21": 1.23,
    "2022-11-22": 1.22,
    "2022-11-23": 1.21,
    "2022-11-24": 1.23,
    "2022-11-25": 1.21,
    "2022-11-28": 1.23,
    "2022-11-29": 1.22,
    "2022-11-30": 1.23,
    "2022-12-01": 1.23
}