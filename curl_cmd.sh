curl -s -k -H 'Content-Type: application/json' \
    -X POST \
     -d '{
        "git_repo":"git@gitlab-ber1.cyren.io:dataservices/template-library/prototypes/single-source-spring-kstream-prototype.git",
        "conf_dir":"/src/main/java/io/cyren/ds/",
        "new_project":"generated-templates"
      }' "http://127.0.0.1:5000/api/v1/template/"

    # templategenerator


# curl -s -k -H 'Content-Type: application/json' \
#     -X POST \
#      -d '{
#         "git_repo":"git@gitlab-ber1.cyren.io:dataservices/template-library/prototypes/single-source-spring-kstream-prototype.git",
#         "conf_dir":"/src/main/java/io/cyren/ds/",
#         "source_template":"git@gitlab-ber1.cyren.io:dataservices/template-library/prototypes",
#         "new_project":"my-new-cool-project"
#       }' "http://127.0.0.1:5000/api/v1/template/"

