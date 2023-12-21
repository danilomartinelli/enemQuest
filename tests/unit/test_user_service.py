import unittest
from unittest.mock import Mock
from app.services.user_service import UserService


class TestUserService(unittest.TestCase):

    def setUp(self):
        self.user_repo = Mock()
        self.user_service = UserService(self.user_repo)

    def test_get_ranking_newbie(self):
        user_id = "user-1"
        self.user_repo.get_user_by_id.return_value = {"_id": user_id, "score": 0}

        ranking = self.user_service.get_ranking(user_id)

        self.assertEqual(ranking["title"], "Novato")

    def test_get_ranking_connoisseur(self):
        user_id = "user-2"
        self.user_repo.get_user_by_id.return_value = {"_id": user_id, "score": 80}

        ranking = self.user_service.get_ranking(user_id)

        self.assertEqual(ranking["title"], "Conhecedor")

    def test_get_ranking_expert(self):
        user_id = "user-3"
        self.user_repo.get_user_by_id.return_value = {"_id": user_id, "score": 150}

        ranking = self.user_service.get_ranking(user_id)

        self.assertEqual(ranking["title"], "Expert")

    def test_get_ranking_master(self):
        user_id = "user-4"
        self.user_repo.get_user_by_id.return_value = {"_id": user_id, "score": 250}

        ranking = self.user_service.get_ranking(user_id)

        self.assertEqual(ranking["title"], "Mestre do ENEM")


if __name__ == '__main__':
    unittest.main()
