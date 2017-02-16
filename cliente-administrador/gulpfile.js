var gulp = require('gulp');
var vulcanize = require('gulp-vulcanize');
var crisper = require('gulp-crisper');
var replace = require('gulp-replace');

gulp.task('vulcanize', function() {
    return gulp.src('elements.html')
        .pipe(vulcanize())
        .pipe(crisper())
        .pipe(replace('src="bower_components', 'src="lib'))
        .pipe(gulp.dest('src/'));
});

gulp.task('default', ['vulcanize']);
