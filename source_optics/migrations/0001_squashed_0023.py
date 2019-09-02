# Generated by Django 2.2.2 on 2019-09-02 12:29

from django.conf import settings
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion
import source_optics.models


class Migration(migrations.Migration):

    replaces = [('source_optics', '0001_initial'), ('source_optics', '0002_auto_20190717_1942'), ('source_optics', '0003_auto_20190722_1719'), ('source_optics', '0004_auto_20190722_1832'), ('source_optics', '0005_auto_20190722_2007'), ('source_optics', '0006_auto_20190723_1350'), ('source_optics', '0007_auto_20190723_1508'), ('source_optics', '0008_auto_20190723_1936'), ('source_optics', '0009_auto_20190724_1632'), ('source_optics', '0010_auto_20190724_1958'), ('source_optics', '0011_auto_20190725_2025'), ('source_optics', '0012_auto_20190726_0134'), ('source_optics', '0013_auto_20190727_0015'), ('source_optics', '0014_auto_20190727_0024'), ('source_optics', '0015_auto_20190727_0056'), ('source_optics', '0016_auto_20190727_0116'), ('source_optics', '0017_auto_20190807_2024'), ('source_optics', '0018_auto_20190810_2225'), ('source_optics', '0019_auto_20190830_2308'), ('source_optics', '0020_statistic_days_before_joined'), ('source_optics', '0021_auto_20190831_2005'), ('source_optics', '0022_auto_20190831_2043'), ('source_optics', '0023_statistic_average_commit_size')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(db_index=True, max_length=64, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sha', models.TextField(db_index=True, max_length=256)),
                ('commit_date', models.DateTimeField(db_index=True, null=True)),
                ('author_date', models.DateTimeField(null=True)),
                ('subject', models.TextField(db_index=True, max_length=256)),
                ('lines_added', models.IntegerField(default=0)),
                ('lines_removed', models.IntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='source_optics.Author')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_index=True, max_length=256, null=True)),
                ('path', models.TextField(db_index=True, max_length=256, null=True)),
                ('ext', models.TextField(max_length=32, null=True)),
                ('binary', models.BooleanField(default=False)),
                ('lines_added', models.IntegerField(default=0)),
                ('lines_removed', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LoginCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=64)),
                ('username', models.TextField(max_length=32)),
                ('password', models.TextField(max_length=128)),
                ('description', models.TextField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=32, unique=True)),
                ('admins', models.ManyToManyField(related_name='admins', to=settings.AUTH_USER_MODEL)),
                ('members', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=True)),
                ('last_scanned', models.DateTimeField(blank=True, null=True)),
                ('last_rollup', models.DateTimeField(blank=True, null=True)),
                ('earliest_commit', models.DateTimeField(blank=True, null=True)),
                ('last_pulled', models.DateTimeField(blank=True, null=True)),
                ('url', models.TextField(max_length=256, unique=True)),
                ('name', models.TextField(db_index=True, max_length=32, unique=True)),
                ('color', models.CharField(blank=True, max_length=10, null=True)),
                ('cred', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='source_optics.LoginCredential')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='source_optics.Organization')),
            ],
            options={
                'verbose_name_plural': 'repositories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, db_index=True, max_length=64, null=True)),
                ('repos', models.ManyToManyField(blank=True, related_name='tagged_repos', to='source_optics.Repository')),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(db_index=True, null=True)),
                ('interval', models.TextField(choices=[('DY', 'Day'), ('WK', 'Week'), ('MN', 'Month')], db_index=True, max_length=5)),
                ('lines_added', models.IntegerField(blank=True, null=True)),
                ('lines_removed', models.IntegerField(blank=True, null=True)),
                ('lines_changed', models.IntegerField(blank=True, null=True)),
                ('commit_total', models.IntegerField(blank=True, null=True)),
                ('files_changed', models.IntegerField(blank=True, null=True)),
                ('author_total', models.IntegerField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='source_optics.Author')),
                ('file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file', to='source_optics.File')),
                ('repo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='repo', to='source_optics.Repository')),
            ],
        ),
        migrations.AddField(
            model_name='repository',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='source_optics.Tag'),
        ),
        migrations.CreateModel(
            name='FileChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_index=True, max_length=256, null=True)),
                ('path', models.TextField(db_index=True, max_length=256, null=True)),
                ('ext', models.TextField(max_length=32)),
                ('binary', models.BooleanField(default=False)),
                ('lines_added', models.IntegerField(default=0)),
                ('lines_removed', models.IntegerField(default=0)),
                ('commit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commit', to='source_optics.Commit')),
                ('repo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filechange_repo', to='source_optics.Repository')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='changes',
            field=models.ManyToManyField(related_name='changes', to='source_optics.FileChange'),
        ),
        migrations.AddField(
            model_name='file',
            name='repo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_repo', to='source_optics.Repository'),
        ),
        migrations.AddField(
            model_name='commit',
            name='files',
            field=models.ManyToManyField(to='source_optics.File'),
        ),
        migrations.AddField(
            model_name='commit',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repos', to='source_optics.Repository'),
        ),
        migrations.AddField(
            model_name='author',
            name='repos',
            field=models.ManyToManyField(related_name='author_repos', to='source_optics.Repository'),
        ),
        migrations.AddIndex(
            model_name='statistic',
            index=models.Index(fields=['interval', 'author', 'repo', 'file', 'start_date'], name='rollup1'),
        ),
        migrations.AddIndex(
            model_name='statistic',
            index=models.Index(fields=['start_date', 'interval', 'repo', 'author'], name='author_rollup'),
        ),
        migrations.AlterUniqueTogether(
            name='statistic',
            unique_together={('start_date', 'interval', 'repo', 'author', 'file')},
        ),
        migrations.AddIndex(
            model_name='commit',
            index=models.Index(fields=['commit_date', 'author', 'repo'], name='source_opti_commit__69e2b7_idx'),
        ),
        migrations.AlterModelOptions(
            name='logincredential',
            options={'verbose_name': 'Credential', 'verbose_name_plural': 'Credentials'},
        ),
        migrations.AddField(
            model_name='logincredential',
            name='ssh_unlock_passphrase',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='author',
            name='repos',
        ),
        migrations.AlterField(
            model_name='commit',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commits', to='source_optics.Author'),
        ),
        migrations.AlterField(
            model_name='commit',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commits', to='source_optics.Repository'),
        ),
        migrations.AlterField(
            model_name='file',
            name='changes',
            field=models.ManyToManyField(related_name='_file_changes_+', to='source_optics.FileChange'),
        ),
        migrations.AlterField(
            model_name='file',
            name='repo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='source_optics.Repository'),
        ),
        migrations.AlterField(
            model_name='filechange',
            name='repo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='source_optics.Repository'),
        ),
        migrations.AlterField(
            model_name='logincredential',
            name='password',
            field=models.TextField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='logincredential',
            name='username',
            field=models.TextField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='organization',
            name='admins',
            field=models.ManyToManyField(related_name='_organization_admins_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(related_name='_organization_members_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tag',
            name='repos',
            field=models.ManyToManyField(blank=True, related_name='_tag_repos_+', to='source_optics.Repository'),
        ),
        migrations.AddField(
            model_name='repository',
            name='force_next_pull',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='logincredential',
            name='ssh_private_key',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_index=True, max_length=64)),
                ('username', models.TextField(blank=True, help_text='for github/gitlab username', max_length=32)),
                ('password', models.TextField(blank=True, help_text='for github/gitlab imports', max_length=128, null=True)),
                ('ssh_private_key', models.TextField(blank=True, help_text='for cloning private repos', null=True)),
                ('ssh_unlock_passphrase', models.TextField(blank=True, help_text='for cloning private repos', null=True)),
                ('description', models.TextField(blank=True, max_length=128, null=True)),
                ('api_endpoint', models.TextField(blank=True, help_text='for github/gitlab imports off private instances', null=True)),
                ('import_filter', models.CharField(blank=True, help_text='if set, only import repos matching this fnmatch pattern', max_length=256, null=True)),
                ('organization_identifier', models.CharField(blank=True, help_text='for github/gitlab imports', max_length=256, null=True)),
            ],
            options={
                'verbose_name': 'Credential',
                'verbose_name_plural': 'Credentials',
            },
        ),
        migrations.RemoveField(
            model_name='repository',
            name='cred',
        ),
        migrations.AlterField(
            model_name='organization',
            name='admins',
            field=models.ManyToManyField(help_text='currently unused', related_name='_organization_admins_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(help_text='currently unused', related_name='_organization_members_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='repository',
            name='enabled',
            field=models.BooleanField(default=True, help_text='if false, disable scanning'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='url',
            field=models.TextField(help_text='use a git ssh url for private repos, else http/s are ok', max_length=256, unique=True),
        ),
        migrations.DeleteModel(
            name='LoginCredential',
        ),
        migrations.AddField(
            model_name='organization',
            name='credential',
            field=models.ForeignKey(help_text='used for repo imports and git checkouts', null=True, on_delete=django.db.models.deletion.SET_NULL, to='source_optics.Credential'),
        ),
        migrations.AddField(
            model_name='organization',
            name='webhook_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organization',
            name='webhook_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='name',
            field=models.TextField(db_index=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='repository',
            name='url',
            field=models.TextField(help_text='use a git ssh url for private repos, else http/s are ok', max_length=255, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='repository',
            unique_together={('name', 'organization')},
        ),
        migrations.AlterField(
            model_name='repository',
            name='name',
            field=models.TextField(db_index=True, max_length=32, validators=[source_optics.models.validate_repo_name]),
        ),
        migrations.AddField(
            model_name='repository',
            name='force_nuclear_rescan',
            field=models.BooleanField(default=False, help_text='on next scan loop, delete all commits/records and rescan everything'),
        ),
        migrations.AlterField(
            model_name='repository',
            name='force_next_pull',
            field=models.BooleanField(default=False, help_text='used by webhooks to signal the scanner'),
        ),
        migrations.AddField(
            model_name='repository',
            name='webhook_token',
            field=models.CharField(blank=True, help_text='prevents against trivial webhook spam', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='scanner_directory_allow_list',
            field=models.TextField(blank=True, help_text='if set, fnmatch patterns of directories to require, one per line', null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='scanner_directory_deny_list',
            field=models.TextField(blank=True, help_text='fnmatch patterns or prefixes of directories to exclude, one per line', null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='scanner_extension_allow_list',
            field=models.TextField(blank=True, help_text='if set, fnmatch patterns of extensions to require, one per line', null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='scanner_extension_deny_list',
            field=models.TextField(blank=True, help_text='fnmatch patterns or prefixes of extensions to exclude, one per line ', null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='checkout_path_override',
            field=models.CharField(blank=True, help_text='if set, override the default checkout location', max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='repository',
            name='scanner_directory_allow_list',
            field=models.TextField(blank=True, help_text='if set, fnmatch patterns of directories to require, one per line', null=True),
        ),
        migrations.AddField(
            model_name='repository',
            name='scanner_directory_deny_list',
            field=models.TextField(blank=True, help_text='fnmatch patterns or prefixes of directories to exclude, one per line', null=True),
        ),
        migrations.AddField(
            model_name='repository',
            name='scanner_extension_allow_list',
            field=models.TextField(blank=True, help_text='if set, fnmatch patterns of extensions to require, one per line', null=True),
        ),
        migrations.AddField(
            model_name='repository',
            name='scanner_extension_deny_list',
            field=models.TextField(blank=True, help_text='fnmatch patterns or prefixes of extensions to exclude, one per line ', null=True),
        ),
        migrations.AlterModelOptions(
            name='repository',
            options={},
        ),
        migrations.AddField(
            model_name='filechange',
            name='file',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='source_optics.File'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.TextField(db_index=True, max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='url',
            field=models.TextField(db_index=True, help_text='use a git ssh url for private repos, else http/s are ok', max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='commit',
            unique_together={('repo', 'sha')},
        ),
        migrations.AlterUniqueTogether(
            name='file',
            unique_together={('repo', 'name', 'path', 'ext')},
        ),
        migrations.AlterUniqueTogether(
            name='filechange',
            unique_together={('file', 'commit')},
        ),
        migrations.AddIndex(
            model_name='author',
            index=models.Index(fields=['email'], name='source_opti_email_d3e229_idx'),
        ),
        migrations.AddIndex(
            model_name='commit',
            index=models.Index(fields=['author_date', 'author', 'repo'], name='source_opti_author__cbf24f_idx'),
        ),
        migrations.AddIndex(
            model_name='repository',
            index=models.Index(fields=['name', 'organization'], name='source_opti_name_5846e6_idx'),
        ),
        migrations.RemoveField(
            model_name='commit',
            name='files',
        ),
        migrations.RemoveField(
            model_name='commit',
            name='lines_added',
        ),
        migrations.RemoveField(
            model_name='commit',
            name='lines_removed',
        ),
        migrations.RemoveField(
            model_name='file',
            name='changes',
        ),
        migrations.RemoveField(
            model_name='file',
            name='lines_added',
        ),
        migrations.RemoveField(
            model_name='file',
            name='lines_removed',
        ),
        migrations.RemoveField(
            model_name='filechange',
            name='binary',
        ),
        migrations.RemoveField(
            model_name='filechange',
            name='ext',
        ),
        migrations.RemoveField(
            model_name='filechange',
            name='name',
        ),
        migrations.RemoveField(
            model_name='filechange',
            name='path',
        ),
        migrations.RemoveField(
            model_name='filechange',
            name='repo',
        ),
        migrations.RemoveIndex(
            model_name='statistic',
            name='rollup1',
        ),
        migrations.RemoveField(
            model_name='repository',
            name='earliest_commit',
        ),
        migrations.RemoveField(
            model_name='repository',
            name='last_rollup',
        ),
        migrations.AlterUniqueTogether(
            name='statistic',
            unique_together={('start_date', 'interval', 'repo', 'author')},
        ),
        migrations.RemoveField(
            model_name='statistic',
            name='file',
        ),
        migrations.AlterModelOptions(
            name='repository',
            options={'verbose_name_plural': 'repositories'},
        ),
        migrations.AlterField(
            model_name='filechange',
            name='commit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_changes', to='source_optics.Commit'),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='interval',
            field=models.TextField(choices=[('DY', 'Day'), ('WK', 'Week'), ('MN', 'Month')], max_length=5),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='file',
            unique_together={('repo', 'name', 'path')},
        ),
        migrations.RemoveIndex(
            model_name='author',
            name='source_opti_email_d3e229_idx',
        ),
        migrations.RemoveIndex(
            model_name='commit',
            name='source_opti_commit__69e2b7_idx',
        ),
        migrations.RemoveIndex(
            model_name='commit',
            name='source_opti_author__cbf24f_idx',
        ),
        migrations.RemoveIndex(
            model_name='statistic',
            name='author_rollup',
        ),
        migrations.AddIndex(
            model_name='commit',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['commit_date', 'author', 'repo'], name='commit1'),
        ),
        migrations.AddIndex(
            model_name='commit',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['author_date', 'author', 'repo'], name='commit2'),
        ),
        migrations.AddIndex(
            model_name='statistic',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['start_date', 'interval', 'repo', 'author'], name='author_rollup2'),
        ),
        migrations.AddIndex(
            model_name='file',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['repo', 'name', 'path'], name='file1'),
        ),
        migrations.AddIndex(
            model_name='filechange',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['file', 'commit'], name='file_change1'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.CharField(db_index=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='commit',
            name='sha',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='commit',
            name='subject',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='credential',
            name='api_endpoint',
            field=models.CharField(blank=True, help_text='for github/gitlab imports off private instances', max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='credential',
            name='description',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='credential',
            name='import_filter',
            field=models.CharField(blank=True, help_text='if set, only import repos matching this fnmatch pattern', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='credential',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='credential',
            name='password',
            field=models.CharField(blank=True, help_text='for github/gitlab imports', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='credential',
            name='ssh_unlock_passphrase',
            field=models.CharField(blank=True, help_text='for cloning private repos', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='credential',
            name='username',
            field=models.CharField(blank=True, help_text='for github/gitlab username', max_length=64),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='repository',
            name='name',
            field=models.CharField(db_index=True, max_length=64, validators=[source_optics.models.validate_repo_name]),
        ),
        migrations.AlterField(
            model_name='repository',
            name='url',
            field=models.CharField(db_index=True, help_text='use a git ssh url for private repos, else http/s are ok', max_length=255),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.CharField(db_index=True, max_length=512, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='commit',
            name='sha',
            field=models.CharField(db_index=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='commit',
            name='subject',
            field=models.TextField(db_index=True),
        ),
        migrations.RemoveField(
            model_name='repository',
            name='color',
        ),
        migrations.AddField(
            model_name='statistic',
            name='days_since_seen',
            field=models.IntegerField(default=-1, null=True),
        ),
        migrations.AddField(
            model_name='statistic',
            name='earliest_commit_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='statistic',
            name='latest_commit_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='statistic',
            name='interval',
            field=models.TextField(choices=[('DY', 'Day'), ('WK', 'Week'), ('MN', 'Month'), ('LF', 'Lifetime')], max_length=5),
        ),
        migrations.AddField(
            model_name='statistic',
            name='days_before_joined',
            field=models.IntegerField(default=-1, null=True),
        ),
        migrations.AddField(
            model_name='statistic',
            name='days_active',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='statistic',
            name='longevity',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='statistic',
            name='days_before_last',
            field=models.IntegerField(default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='filechange',
            name='file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_changes', to='source_optics.File'),
        ),
        migrations.AddField(
            model_name='statistic',
            name='average_commit_size',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]