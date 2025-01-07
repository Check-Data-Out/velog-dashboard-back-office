# Generated by Django 5.1.4 on 2025-01-07 13:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracking", "0004_remove_userstaytime_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="usereventtracking",
            name="request_header",
            field=models.JSONField(default=dict, verbose_name="요청 헤더"),
        ),
        migrations.AlterField(
            model_name="usereventtracking",
            name="event_type",
            field=models.CharField(
                choices=[
                    ("11", "로그인 성공"),
                    ("12", "페이지 이동"),
                    ("13", "로그아웃"),
                    ("21", "메인(통계 블록 열림/닫힘)"),
                    ("22", "메인(정렬 선택)"),
                    ("23", "메인(새로고침)"),
                    ("31", "리더보드(정렬 선택)"),
                    ("99", "nothing"),
                ],
                default="99",
                help_text="어떤 이벤트 타입인지 저장하는 필드입니다.",
                max_length=2,
                verbose_name="이벤트타입",
            ),
        ),
    ]
