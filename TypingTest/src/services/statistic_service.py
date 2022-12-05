from entities.statistic import Statistic
from services.user_service import user_service

from repositories.statistics_repository import (
    statistics_repository as default_statistic_repository
)

class StatisticService:
    def __init__(self, statistic_repository = default_statistic_repository):
        self.round_statistic = None
        self.statistic_repository = statistic_repository

    def get_round_statistic(self):
        return self.round_statistic

    def set_round_statistic(self, statistic):
        self.round_statistic = statistic

    def get_current_user_statistic(self):

        user = user_service.get_current_user()
        username = user.username

        return self.statistic_repository.find_user_statistics(username)

    def update_user_total_statistics(self):

        old_statistics = self.get_current_user_statistic()

        if old_statistics is None:
            self.statistic_repository.insert_user_statistics(self.round_statistic)
            return self.round_statistic

        new_statistic = self.calculate_total_statistic(old_statistics)
        self.statistic_repository.update_user_statistics(new_statistic)

        return new_statistic

    def delete_all_statistics(self):
        self.statistic_repository.delete_all_statistics()

    def calculate_total_statistic(self, old_statistics):

        old_total = old_statistics.total

        new_total = old_statistics.total + self.round_statistic.total

        new_accuracy = self.calculate_new_average(old_total,
                                                new_total,
                                                old_statistics.accuracy,
                                                self.round_statistic.accuracy)

        new_wpm = self.calculate_new_average(old_total,
                                            new_total,
                                            old_statistics.wpm,
                                            self.round_statistic.wpm)

        new_time_taken = self.calculate_new_average(old_total,
                                            new_total,
                                            old_statistics.time_taken,
                                            self.round_statistic.time_taken)

        new_max_wpm = max(old_statistics.max_wpm, self.round_statistic.wpm)

        new_slowest_wpm = min(old_statistics.min_wpm, self.round_statistic.wpm)

        return Statistic(self.round_statistic.username,
                        new_accuracy,
                        new_wpm,
                        new_time_taken,
                        new_total,
                        new_max_wpm,
                        new_slowest_wpm)

    def calculate_new_average(self, old_total, new_total, old_stat, new_stat):

        return (old_total*old_stat+new_stat)/new_total

statistic_service = StatisticService()
