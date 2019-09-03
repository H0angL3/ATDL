'use strict';

module.exports = function (grunt) {

    // Load grunt tasks automatically
    require('load-grunt-tasks')(grunt);

    // Time how long tasks take. Can help when optimizing build times
    require('time-grunt')(grunt);

    // Configurable paths
    var config = {
        app: 'src',
        tmp: 'tmp',
        dist: 'dist'
    };

    // Define the configuration for all the tasks
    grunt.initConfig({

        // Load package.json
        pkg: grunt.file.readJSON('package.json'),

        // Project settings
        config: config,

        // Watches files for changes and runs tasks based on the changed files
        watch: {
            js: {
                files: ['<%= config.app %>/js/{,*/}*.js'],
                tasks: ['jshint']
            },
            gruntfile: {
                files: ['Gruntfile.js']
            },
            styles: {
                files: ['<%= config.app %>/less/{,*/}*.css']
            }
        },

        // Empties folders
        clean: {
            dist: {
                files: [{
                    dot: true,
                    src: [
                        '<%= config.dist %>/*',
                        '!<%= config.dist %>/.git*'
                    ]
                }]
            },
            tmp: {
                files: [{
                    dot: true,
                    src: [
                        '<%= config.tmp %>'
                    ]
                }]
            }
        },

        // Make sure code styles are up to par and there are no obvious mistakes
        jshint: {
            options: {
                jshintrc: '.jshintrc',
                reporter: require('jshint-stylish')
            },
            all: [
                'Gruntfile.js',
                '<%= config.app %>/js/*.js'
            ]
        },

        // Create tmp folder
        createtmp: grunt.file.mkdir(config.tmp),

        // Less compiling
        recess: {
            options: {
                compile: true
            },
            dist: {
                files: [{
                    expand: true,
                    cwd: '<%= config.app %>/less',
                    src: '{,*/}*.less',
                    dest: '<%= config.tmp %>/css/',
                    ext: '.css'
                }]
            }
        },

        // Cssmin
        cssmin: {
            minify: {
                expand: true,
                cwd: '<%= config.tmp %>/css/',
                src: ['*.css', '!*.min.css'],
                dest: '<%= config.dist %>/css/',
                ext: '.min.css'
            }
        },

        // Concat
        concat: {
            options: {
                separator: ';'
            },
            dist: {
                src: ['<%= config.app %>/js/*.js'],
                // the location of the resulting JS file
                dest: '<%= config.tmp %>/js/<%= pkg.name %>.js'
            }
        },

        // Uglify
        uglify: {
            dist: {
                files: {
                    '<%= config.dist %>/js/<%= pkg.name %>.min.js': ['<%= concat.dist.dest %>']
                }
            }
        }

    });

    grunt.registerTask('build', [
        'clean:dist',
        'recess',
        'cssmin',
        'concat',
        'uglify',
        'clean:tmp'
    ]);

    grunt.registerTask('default', [
        'newer:jshint',
        'build'
    ]);
};
