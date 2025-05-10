from django.test import TestCase
from django.contrib.auth import get_user_model
from movies.models import Movie
from reviews.models import Review, ReviewComment

User = get_user_model()

class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='tester',
            email='tester@example.com',
            password='pass1234'
        )
        self.movie = Movie.objects.create(title='테스트 영화', description='설명', release_date='2024-01-01')

    def test_review_creation(self):
        review = Review.objects.create(user=self.user, movie=self.movie, rating=5, comment='재밌었어요!')
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, '재밌었어요!')
        self.assertEqual(str(review), f"{self.user.username} - {self.movie.title} ({review.rating}점)")

    def test_review_deletion_updates_average_rating(self):
        Review.objects.create(user=self.user, movie=self.movie, rating=4)
        Review.objects.create(user=self.user, movie=self.movie, rating=2)
        self.movie.update_average_rating()
        self.assertEqual(self.movie.average_rating_cache, 3.0)
        Review.objects.first().delete()
        self.movie.update_average_rating()
        self.assertEqual(self.movie.average_rating_cache, 2.0)

class ReviewCommentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='commenter',
            email='commenter@example.com',
            password='pass1234'
        )
        self.movie = Movie.objects.create(title='댓글 테스트 영화', description='설명', release_date='2024-01-01')
        self.review = Review.objects.create(user=self.user, movie=self.movie, rating=4, comment='괜찮아요')

    def test_comment_creation(self):
        comment = ReviewComment.objects.create(user=self.user, review=self.review, content='동의합니다')
        self.assertEqual(comment.review, self.review)
        self.assertEqual(comment.content, '동의합니다')
        self.assertEqual(str(comment), f"{self.user.username}: {comment.content[:20]}")