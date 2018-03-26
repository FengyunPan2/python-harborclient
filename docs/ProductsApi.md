# swagger_client.ProductsApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurations_get**](ProductsApi.md#configurations_get) | **GET** /configurations | Get system configurations.
[**configurations_put**](ProductsApi.md#configurations_put) | **PUT** /configurations | Modify system configurations.
[**configurations_reset_post**](ProductsApi.md#configurations_reset_post) | **POST** /configurations/reset | Reset system configurations.
[**email_ping_post**](ProductsApi.md#email_ping_post) | **POST** /email/ping | Test connection and authentication with email server.
[**internal_syncregistry_post**](ProductsApi.md#internal_syncregistry_post) | **POST** /internal/syncregistry | Sync repositories from registry to DB.
[**jobs_replication_get**](ProductsApi.md#jobs_replication_get) | **GET** /jobs/replication | List filters jobs according to the policy and repository
[**jobs_replication_id_delete**](ProductsApi.md#jobs_replication_id_delete) | **DELETE** /jobs/replication/{id} | Delete specific ID job.
[**jobs_replication_id_log_get**](ProductsApi.md#jobs_replication_id_log_get) | **GET** /jobs/replication/{id}/log | Get job logs.
[**jobs_scan_id_log_get**](ProductsApi.md#jobs_scan_id_log_get) | **GET** /jobs/scan/{id}/log | Get job logs.
[**ldap_ping_post**](ProductsApi.md#ldap_ping_post) | **POST** /ldap/ping | Ping available ldap service.
[**ldap_users_import_post**](ProductsApi.md#ldap_users_import_post) | **POST** /ldap/users/import | Import selected available ldap users.
[**ldap_users_search_post**](ProductsApi.md#ldap_users_search_post) | **POST** /ldap/users/search | Search available ldap users.
[**logs_get**](ProductsApi.md#logs_get) | **GET** /logs | Get recent logs of the projects which the user is a member of
[**policies_replication_get**](ProductsApi.md#policies_replication_get) | **GET** /policies/replication | List filters policies by name and project_id
[**policies_replication_id_enablement_put**](ProductsApi.md#policies_replication_id_enablement_put) | **PUT** /policies/replication/{id}/enablement | Put modifies enablement of the policy.
[**policies_replication_id_get**](ProductsApi.md#policies_replication_id_get) | **GET** /policies/replication/{id} | Get replication policy.
[**policies_replication_id_put**](ProductsApi.md#policies_replication_id_put) | **PUT** /policies/replication/{id} | Put modifies name, description, target and enablement of policy.
[**policies_replication_post**](ProductsApi.md#policies_replication_post) | **POST** /policies/replication | Post creates a policy
[**projects_get**](ProductsApi.md#projects_get) | **GET** /projects | List projects
[**projects_head**](ProductsApi.md#projects_head) | **HEAD** /projects | Check if the project name user provided already exists.
[**projects_post**](ProductsApi.md#projects_post) | **POST** /projects | Create a new project.
[**projects_project_id_delete**](ProductsApi.md#projects_project_id_delete) | **DELETE** /projects/{project_id} | Delete project by projectID
[**projects_project_id_get**](ProductsApi.md#projects_project_id_get) | **GET** /projects/{project_id} | Return specific project detail infomation
[**projects_project_id_logs_get**](ProductsApi.md#projects_project_id_logs_get) | **GET** /projects/{project_id}/logs | Get access logs accompany with a relevant project.
[**projects_project_id_members_get**](ProductsApi.md#projects_project_id_members_get) | **GET** /projects/{project_id}/members/ | Return a project&#39;s relevant role members.
[**projects_project_id_members_post**](ProductsApi.md#projects_project_id_members_post) | **POST** /projects/{project_id}/members/ | Add project role member accompany with relevant project and user.
[**projects_project_id_members_user_id_delete**](ProductsApi.md#projects_project_id_members_user_id_delete) | **DELETE** /projects/{project_id}/members/{user_id} | Delete project role members accompany with relevant project and user.
[**projects_project_id_members_user_id_get**](ProductsApi.md#projects_project_id_members_user_id_get) | **GET** /projects/{project_id}/members/{user_id} | Return role members accompany with relevant project and user.
[**projects_project_id_members_user_id_put**](ProductsApi.md#projects_project_id_members_user_id_put) | **PUT** /projects/{project_id}/members/{user_id} | Update project role members accompany with relevant project and user.
[**projects_project_id_publicity_put**](ProductsApi.md#projects_project_id_publicity_put) | **PUT** /projects/{project_id}/publicity | Update properties for a selected project.
[**repositories_get**](ProductsApi.md#repositories_get) | **GET** /repositories | Get repositories accompany with relevant project and repo name.
[**repositories_repo_name_delete**](ProductsApi.md#repositories_repo_name_delete) | **DELETE** /repositories/{repo_name} | Delete a repository.
[**repositories_repo_name_signatures_get**](ProductsApi.md#repositories_repo_name_signatures_get) | **GET** /repositories/{repo_name}/signatures | Get signature information of a repository
[**repositories_repo_name_tags_get**](ProductsApi.md#repositories_repo_name_tags_get) | **GET** /repositories/{repo_name}/tags | Get tags of a relevant repository.
[**repositories_repo_name_tags_tag_delete**](ProductsApi.md#repositories_repo_name_tags_tag_delete) | **DELETE** /repositories/{repo_name}/tags/{tag} | Delete a tag in a repository.
[**repositories_repo_name_tags_tag_get**](ProductsApi.md#repositories_repo_name_tags_tag_get) | **GET** /repositories/{repo_name}/tags/{tag} | Get the tag of the repository.
[**repositories_repo_name_tags_tag_manifest_get**](ProductsApi.md#repositories_repo_name_tags_tag_manifest_get) | **GET** /repositories/{repo_name}/tags/{tag}/manifest | Get manifests of a relevant repository.
[**repositories_repo_name_tags_tag_scan_post**](ProductsApi.md#repositories_repo_name_tags_tag_scan_post) | **POST** /repositories/{repo_name}/tags/{tag}/scan | Scan the image.
[**repositories_repo_name_tags_tag_vulnerability_details_get**](ProductsApi.md#repositories_repo_name_tags_tag_vulnerability_details_get) | **GET** /repositories/{repo_name}/tags/{tag}/vulnerability/details | Get vulnerability details of the image.
[**repositories_top_get**](ProductsApi.md#repositories_top_get) | **GET** /repositories/top | Get public repositories which are accessed most.
[**search_get**](ProductsApi.md#search_get) | **GET** /search | Search for projects and repositories
[**statistics_get**](ProductsApi.md#statistics_get) | **GET** /statistics | Get projects number and repositories number relevant to the user
[**systeminfo_get**](ProductsApi.md#systeminfo_get) | **GET** /systeminfo | Get general system info
[**systeminfo_getcert_get**](ProductsApi.md#systeminfo_getcert_get) | **GET** /systeminfo/getcert | Get default root certificate under OVA deployment.
[**systeminfo_volumes_get**](ProductsApi.md#systeminfo_volumes_get) | **GET** /systeminfo/volumes | Get system volume info (total/free size).
[**targets_get**](ProductsApi.md#targets_get) | **GET** /targets | List filters targets by name.
[**targets_id_delete**](ProductsApi.md#targets_id_delete) | **DELETE** /targets/{id} | Delete specific replication&#39;s target.
[**targets_id_get**](ProductsApi.md#targets_id_get) | **GET** /targets/{id} | Get replication&#39;s target.
[**targets_id_ping_post**](ProductsApi.md#targets_id_ping_post) | **POST** /targets/{id}/ping | Ping target.
[**targets_id_policies_get**](ProductsApi.md#targets_id_policies_get) | **GET** /targets/{id}/policies/ | List the target relevant policies.
[**targets_id_put**](ProductsApi.md#targets_id_put) | **PUT** /targets/{id} | Update replication&#39;s target.
[**targets_ping_post**](ProductsApi.md#targets_ping_post) | **POST** /targets/ping | Ping validates target.
[**targets_post**](ProductsApi.md#targets_post) | **POST** /targets | Create a new replication target.
[**users_current_get**](ProductsApi.md#users_current_get) | **GET** /users/current | Get current user info.
[**users_get**](ProductsApi.md#users_get) | **GET** /users | Get registered users of Harbor.
[**users_post**](ProductsApi.md#users_post) | **POST** /users | Creates a new user account.
[**users_user_id_delete**](ProductsApi.md#users_user_id_delete) | **DELETE** /users/{user_id} | Mark a registered user as be removed.
[**users_user_id_get**](ProductsApi.md#users_user_id_get) | **GET** /users/{user_id} | Get a user&#39;s profile.
[**users_user_id_password_put**](ProductsApi.md#users_user_id_password_put) | **PUT** /users/{user_id}/password | Change the password on a user that already exists.
[**users_user_id_put**](ProductsApi.md#users_user_id_put) | **PUT** /users/{user_id} | Update a registered user to change his profile.
[**users_user_id_sysadmin_put**](ProductsApi.md#users_user_id_sysadmin_put) | **PUT** /users/{user_id}/sysadmin | Update a registered user to change to be an administrator of Harbor.


# **configurations_get**
> Configurations configurations_get()

Get system configurations.

This endpoint is for retrieving system configurations that only provides for admin user. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()

try: 
    # Get system configurations.
    api_response = api_instance.configurations_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->configurations_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Configurations**](Configurations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configurations_put**
> configurations_put(configurations)

Modify system configurations.

This endpoint is for modifying system configurations that only provides for admin user. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
configurations = swagger_client.Configurations() # Configurations | The configuration map can contain a subset of the attributes of the schema, which are to be updated.

try: 
    # Modify system configurations.
    api_instance.configurations_put(configurations)
except ApiException as e:
    print("Exception when calling ProductsApi->configurations_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configurations** | [**Configurations**](Configurations.md)| The configuration map can contain a subset of the attributes of the schema, which are to be updated. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configurations_reset_post**
> configurations_reset_post()

Reset system configurations.

Reset system configurations from environment variables. Can only be accessed by admin user. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()

try: 
    # Reset system configurations.
    api_instance.configurations_reset_post()
except ApiException as e:
    print("Exception when calling ProductsApi->configurations_reset_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_ping_post**
> email_ping_post(settings=settings)

Test connection and authentication with email server.

Test connection and authentication with email server.  

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
settings = swagger_client.EmailServerSetting() # EmailServerSetting | Email server settings, if some of the settings are not assigned, they will be read from system configuration. (optional)

try: 
    # Test connection and authentication with email server.
    api_instance.email_ping_post(settings=settings)
except ApiException as e:
    print("Exception when calling ProductsApi->email_ping_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings** | [**EmailServerSetting**](EmailServerSetting.md)| Email server settings, if some of the settings are not assigned, they will be read from system configuration. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **internal_syncregistry_post**
> internal_syncregistry_post()

Sync repositories from registry to DB.

This endpoint is for syncing all repositories of registry with database.  

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()

try: 
    # Sync repositories from registry to DB.
    api_instance.internal_syncregistry_post()
except ApiException as e:
    print("Exception when calling ProductsApi->internal_syncregistry_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_replication_get**
> list[JobStatus] jobs_replication_get(policy_id, num=num, end_time=end_time, start_time=start_time, repository=repository, status=status, page=page, page_size=page_size)

List filters jobs according to the policy and repository

This endpoint let user list filters jobs according to the policy and repository. (if start_time and end_time are both null, list jobs of last 10 days) 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
policy_id = 56 # int | The ID of the policy that triggered this job.
num = 56 # int | The return list length number. (optional)
end_time = 789 # int | The end time of jobs done. (Timestamp) (optional)
start_time = 789 # int | The start time of jobs. (Timestamp) (optional)
repository = 'repository_example' # str | The respond jobs list filter by repository name. (optional)
status = 'status_example' # str | The respond jobs list filter by status. (optional)
page = 56 # int | The page nubmer, default is 1. (optional)
page_size = 56 # int | The size of per page, default is 10, maximum is 100. (optional)

try: 
    # List filters jobs according to the policy and repository
    api_response = api_instance.jobs_replication_get(policy_id, num=num, end_time=end_time, start_time=start_time, repository=repository, status=status, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->jobs_replication_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_id** | **int**| The ID of the policy that triggered this job. | 
 **num** | **int**| The return list length number. | [optional] 
 **end_time** | **int**| The end time of jobs done. (Timestamp) | [optional] 
 **start_time** | **int**| The start time of jobs. (Timestamp) | [optional] 
 **repository** | **str**| The respond jobs list filter by repository name. | [optional] 
 **status** | **str**| The respond jobs list filter by status. | [optional] 
 **page** | **int**| The page nubmer, default is 1. | [optional] 
 **page_size** | **int**| The size of per page, default is 10, maximum is 100. | [optional] 

### Return type

[**list[JobStatus]**](JobStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_replication_id_delete**
> jobs_replication_id_delete(id)

Delete specific ID job.

This endpoint is aimed to remove specific ID job from jobservice. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
id = 789 # int | Delete job ID.

try: 
    # Delete specific ID job.
    api_instance.jobs_replication_id_delete(id)
except ApiException as e:
    print("Exception when calling ProductsApi->jobs_replication_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Delete job ID. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_replication_id_log_get**
> jobs_replication_id_log_get(id)

Get job logs.

This endpoint let user search job logs filtered by specific ID. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
id = 789 # int | Relevant job ID

try: 
    # Get job logs.
    api_instance.jobs_replication_id_log_get(id)
except ApiException as e:
    print("Exception when calling ProductsApi->jobs_replication_id_log_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Relevant job ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_scan_id_log_get**
> jobs_scan_id_log_get(id)

Get job logs.

This endpoint let user get scan job logs filtered by specific ID. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
id = 789 # int | Relevant job ID

try: 
    # Get job logs.
    api_instance.jobs_scan_id_log_get(id)
except ApiException as e:
    print("Exception when calling ProductsApi->jobs_scan_id_log_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Relevant job ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_ping_post**
> ldap_ping_post(ldapconf=ldapconf)

Ping available ldap service.

This endpoint ping the available ldap service for test related configuration parameters.  

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
ldapconf = swagger_client.LdapConf() # LdapConf | ldap configuration. support input ldap service configuration. If it's a empty request, will load current configuration from the system. (optional)

try: 
    # Ping available ldap service.
    api_instance.ldap_ping_post(ldapconf=ldapconf)
except ApiException as e:
    print("Exception when calling ProductsApi->ldap_ping_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldapconf** | [**LdapConf**](LdapConf.md)| ldap configuration. support input ldap service configuration. If it&#39;s a empty request, will load current configuration from the system. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_users_import_post**
> ldap_users_import_post(uid_list)

Import selected available ldap users.

This endpoint adds the selected available ldap users to harbor based on related configuration parameters from the system. System will try to guess the user email address and realname, add to harbor user information.  If have errors when import user, will return the list of importing failed uid and the failed reason. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
uid_list = swagger_client.LdapImportUsers() # LdapImportUsers | The uid listed for importing. This list will check users validity of ldap service based on configuration from the system.

try: 
    # Import selected available ldap users.
    api_instance.ldap_users_import_post(uid_list)
except ApiException as e:
    print("Exception when calling ProductsApi->ldap_users_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid_list** | [**LdapImportUsers**](LdapImportUsers.md)| The uid listed for importing. This list will check users validity of ldap service based on configuration from the system. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ldap_users_search_post**
> list[LdapUsers] ldap_users_search_post(username=username, ldap_conf=ldap_conf)

Search available ldap users.

This endpoint searches the available ldap users based on related configuration parameters. Support searched by input ladp configuration, load configuration from the system and specific filter. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
username = 'username_example' # str | Registered user ID (optional)
ldap_conf = swagger_client.LdapConf() # LdapConf | ldap search configuration. ldapconf field can input ldap service configuration. If this item are blank, will load default configuration will load current configuration from the system. (optional)

try: 
    # Search available ldap users.
    api_response = api_instance.ldap_users_search_post(username=username, ldap_conf=ldap_conf)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->ldap_users_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Registered user ID | [optional] 
 **ldap_conf** | [**LdapConf**](LdapConf.md)| ldap search configuration. ldapconf field can input ldap service configuration. If this item are blank, will load default configuration will load current configuration from the system. | [optional] 

### Return type

[**list[LdapUsers]**](LdapUsers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logs_get**
> list[AccessLog] logs_get(username=username, repository=repository, tag=tag, operation=operation, begin_timestamp=begin_timestamp, end_timestamp=end_timestamp, page=page, page_size=page_size)

Get recent logs of the projects which the user is a member of

This endpoint let user see the recent operation logs of the projects which he is member of  

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
username = 'username_example' # str | Username of the operator. (optional)
repository = 'repository_example' # str | The name of repository (optional)
tag = 'tag_example' # str | The name of tag (optional)
operation = 'operation_example' # str | The operation (optional)
begin_timestamp = 'begin_timestamp_example' # str | The begin timestamp (optional)
end_timestamp = 'end_timestamp_example' # str | The end timestamp (optional)
page = 56 # int | The page nubmer, default is 1. (optional)
page_size = 56 # int | The size of per page, default is 10, maximum is 100. (optional)

try: 
    # Get recent logs of the projects which the user is a member of
    api_response = api_instance.logs_get(username=username, repository=repository, tag=tag, operation=operation, begin_timestamp=begin_timestamp, end_timestamp=end_timestamp, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->logs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username of the operator. | [optional] 
 **repository** | **str**| The name of repository | [optional] 
 **tag** | **str**| The name of tag | [optional] 
 **operation** | **str**| The operation | [optional] 
 **begin_timestamp** | **str**| The begin timestamp | [optional] 
 **end_timestamp** | **str**| The end timestamp | [optional] 
 **page** | **int**| The page nubmer, default is 1. | [optional] 
 **page_size** | **int**| The size of per page, default is 10, maximum is 100. | [optional] 

### Return type

[**list[AccessLog]**](AccessLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_replication_get**
> list[RepPolicy] policies_replication_get(name=name, project_id=project_id)

List filters policies by name and project_id

This endpoint let user list filters policies by name and project_id, if name and project_id are nil, list returns all policies 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
name = 'name_example' # str | The replication's policy name. (optional)
project_id = 789 # int | Relevant project ID. (optional)

try: 
    # List filters policies by name and project_id
    api_response = api_instance.policies_replication_get(name=name, project_id=project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->policies_replication_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The replication&#39;s policy name. | [optional] 
 **project_id** | **int**| Relevant project ID. | [optional] 

### Return type

[**list[RepPolicy]**](RepPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_replication_id_enablement_put**
> policies_replication_id_enablement_put(id, enabledflag)

Put modifies enablement of the policy.

This endpoint let user update policy enablement flag. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
id = 789 # int | policy ID
enabledflag = swagger_client.RepPolicyEnablementReq() # RepPolicyEnablementReq | The policy enablement flag.

try: 
    # Put modifies enablement of the policy.
    api_instance.policies_replication_id_enablement_put(id, enabledflag)
except ApiException as e:
    print("Exception when calling ProductsApi->policies_replication_id_enablement_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| policy ID | 
 **enabledflag** | [**RepPolicyEnablementReq**](RepPolicyEnablementReq.md)| The policy enablement flag. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_replication_id_get**
> RepPolicy policies_replication_id_get(id)

Get replication policy.

This endpoint let user search replication policy by specific ID. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
id = 789 # int | policy ID

try: 
    # Get replication policy.
    api_response = api_instance.policies_replication_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->policies_replication_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| policy ID | 

### Return type

[**RepPolicy**](RepPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_replication_id_put**
> policies_replication_id_put(id, policyupdate)

Put modifies name, description, target and enablement of policy.

This endpoint let user update policy name, description, target and enablement. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
id = 789 # int | policy ID
policyupdate = swagger_client.RepPolicyUpdate() # RepPolicyUpdate | Update policy name, description, target and enablement.

try: 
    # Put modifies name, description, target and enablement of policy.
    api_instance.policies_replication_id_put(id, policyupdate)
except ApiException as e:
    print("Exception when calling ProductsApi->policies_replication_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| policy ID | 
 **policyupdate** | [**RepPolicyUpdate**](RepPolicyUpdate.md)| Update policy name, description, target and enablement. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_replication_post**
> policies_replication_post(policyinfo)

Post creates a policy

This endpoint let user creates a policy, and if it is enabled, the replication will be triggered right now. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
policyinfo = swagger_client.RepPolicyPost() # RepPolicyPost | Create new policy.

try: 
    # Post creates a policy
    api_instance.policies_replication_post(policyinfo)
except ApiException as e:
    print("Exception when calling ProductsApi->policies_replication_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policyinfo** | [**RepPolicyPost**](RepPolicyPost.md)| Create new policy. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get**
> list[Project] projects_get(name=name, public=public, owner=owner, page=page, page_size=page_size)

List projects

This endpoint returns all projects created by Harbor, and can be filtered by project name. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
name = 'name_example' # str | The name of project. (optional)
public = true # bool | The project is public or private. (optional)
owner = 'owner_example' # str | The name of project owner. (optional)
page = 56 # int | The page nubmer, default is 1. (optional)
page_size = 56 # int | The size of per page, default is 10, maximum is 100. (optional)

try: 
    # List projects
    api_response = api_instance.projects_get(name=name, public=public, owner=owner, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of project. | [optional] 
 **public** | **bool**| The project is public or private. | [optional] 
 **owner** | **str**| The name of project owner. | [optional] 
 **page** | **int**| The page nubmer, default is 1. | [optional] 
 **page_size** | **int**| The size of per page, default is 10, maximum is 100. | [optional] 

### Return type

[**list[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_head**
> projects_head(project_name)

Check if the project name user provided already exists.

This endpoint is used to check if the project name user provided already exist. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
project_name = 'project_name_example' # str | Project name for checking exists.

try: 
    # Check if the project name user provided already exists.
    api_instance.projects_head(project_name)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_head: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_name** | **str**| Project name for checking exists. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_post**
> projects_post(project)

Create a new project.

This endpoint is for user to create a new project. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
project = swagger_client.ProjectReq() # ProjectReq | New created project.

try: 
    # Create a new project.
    api_instance.projects_post(project)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**ProjectReq**](ProjectReq.md)| New created project. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_delete**
> projects_project_id_delete(project_id)

Delete project by projectID

This endpoint is aimed to delete project by project ID. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
project_id = 789 # int | Project ID of project which will be deleted.

try: 
    # Delete project by projectID
    api_instance.projects_project_id_delete(project_id)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID of project which will be deleted. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_get**
> Project projects_project_id_get(project_id)

Return specific project detail infomation

This endpoint returns specific project information by project ID. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
project_id = 789 # int | Project ID for filtering results.

try: 
    # Return specific project detail infomation
    api_response = api_instance.projects_project_id_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Project ID for filtering results. | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_logs_get**
> list[AccessLog] projects_project_id_logs_get(project_id, username=username, repository=repository, tag=tag, operation=operation, begin_timestamp=begin_timestamp, end_timestamp=end_timestamp, page=page, page_size=page_size)

Get access logs accompany with a relevant project.

This endpoint let user search access logs filtered by operations and date time ranges. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
project_id = 789 # int | Relevant project ID
username = 'username_example' # str | Username of the operator. (optional)
repository = 'repository_example' # str | The name of repository (optional)
tag = 'tag_example' # str | The name of tag (optional)
operation = 'operation_example' # str | The operation (optional)
begin_timestamp = 'begin_timestamp_example' # str | The begin timestamp (optional)
end_timestamp = 'end_timestamp_example' # str | The end timestamp (optional)
page = 56 # int | The page nubmer, default is 1. (optional)
page_size = 56 # int | The size of per page, default is 10, maximum is 100. (optional)

try: 
    # Get access logs accompany with a relevant project.
    api_response = api_instance.projects_project_id_logs_get(project_id, username=username, repository=repository, tag=tag, operation=operation, begin_timestamp=begin_timestamp, end_timestamp=end_timestamp, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_logs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID | 
 **username** | **str**| Username of the operator. | [optional] 
 **repository** | **str**| The name of repository | [optional] 
 **tag** | **str**| The name of tag | [optional] 
 **operation** | **str**| The operation | [optional] 
 **begin_timestamp** | **str**| The begin timestamp | [optional] 
 **end_timestamp** | **str**| The end timestamp | [optional] 
 **page** | **int**| The page nubmer, default is 1. | [optional] 
 **page_size** | **int**| The size of per page, default is 10, maximum is 100. | [optional] 

### Return type

[**list[AccessLog]**](AccessLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_members_get**
> list[User] projects_project_id_members_get(project_id)

Return a project's relevant role members.

This endpoint is for user to search a specified project's relevant role members. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
project_id = 789 # int | Relevant project ID.

try: 
    # Return a project's relevant role members.
    api_response = api_instance.projects_project_id_members_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_members_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_members_post**
> projects_project_id_members_post(project_id, roles=roles)

Add project role member accompany with relevant project and user.

This endpoint is for user to add project role member accompany with relevant project and user. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
project_id = 789 # int | Relevant project ID.
roles = swagger_client.RoleParam() # RoleParam | Role members for adding to relevant project. Only one role is supported in the role list. (optional)

try: 
    # Add project role member accompany with relevant project and user.
    api_instance.projects_project_id_members_post(project_id, roles=roles)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_members_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **roles** | [**RoleParam**](RoleParam.md)| Role members for adding to relevant project. Only one role is supported in the role list. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_members_user_id_delete**
> projects_project_id_members_user_id_delete(project_id, user_id)

Delete project role members accompany with relevant project and user.

This endpoint is aimed to remove project role members already added to the relevant project and user. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
project_id = 789 # int | Relevant project ID.
user_id = 56 # int | Relevant user ID.

try: 
    # Delete project role members accompany with relevant project and user.
    api_instance.projects_project_id_members_user_id_delete(project_id, user_id)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_members_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **user_id** | **int**| Relevant user ID. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_members_user_id_get**
> list[Role] projects_project_id_members_user_id_get(project_id, user_id)

Return role members accompany with relevant project and user.

This endpoint is for user to get role members accompany with relevant project and user.  

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
project_id = 789 # int | Relevant project ID
user_id = 56 # int | Relevant user ID

try: 
    # Return role members accompany with relevant project and user.
    api_response = api_instance.projects_project_id_members_user_id_get(project_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_members_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID | 
 **user_id** | **int**| Relevant user ID | 

### Return type

[**list[Role]**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_members_user_id_put**
> projects_project_id_members_user_id_put(project_id, user_id, roles=roles)

Update project role members accompany with relevant project and user.

This endpoint is for user to update current project role members accompany with relevant project and user. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
project_id = 789 # int | Relevant project ID.
user_id = 56 # int | Relevant user ID.
roles = swagger_client.RoleParam() # RoleParam | Updates for roles and username. (optional)

try: 
    # Update project role members accompany with relevant project and user.
    api_instance.projects_project_id_members_user_id_put(project_id, user_id, roles=roles)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_members_user_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **user_id** | **int**| Relevant user ID. | 
 **roles** | [**RoleParam**](RoleParam.md)| Updates for roles and username. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_publicity_put**
> projects_project_id_publicity_put(project_id, project)

Update properties for a selected project.

This endpoint is aimed to toggle a project publicity status. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
project_id = 789 # int | Selected project ID.
project = swagger_client.Project() # Project | Updates of project.

try: 
    # Update properties for a selected project.
    api_instance.projects_project_id_publicity_put(project_id, project)
except ApiException as e:
    print("Exception when calling ProductsApi->projects_project_id_publicity_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Selected project ID. | 
 **project** | [**Project**](Project.md)| Updates of project. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_get**
> list[Repository] repositories_get(project_id, q=q, page=page, page_size=page_size)

Get repositories accompany with relevant project and repo name.

This endpoint let user search repositories accompanying with relevant project ID and repo name. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
project_id = 56 # int | Relevant project ID.
q = 'q_example' # str | Repo name for filtering results. (optional)
page = 56 # int | The page nubmer, default is 1. (optional)
page_size = 56 # int | The size of per page, default is 10, maximum is 100. (optional)

try: 
    # Get repositories accompany with relevant project and repo name.
    api_response = api_instance.repositories_get(project_id, q=q, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **q** | **str**| Repo name for filtering results. | [optional] 
 **page** | **int**| The page nubmer, default is 1. | [optional] 
 **page_size** | **int**| The size of per page, default is 10, maximum is 100. | [optional] 

### Return type

[**list[Repository]**](Repository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_delete**
> repositories_repo_name_delete(repo_name)

Delete a repository.

This endpoint let user delete a repository with name. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
repo_name = 'repo_name_example' # str | The name of repository which will be deleted.

try: 
    # Delete a repository.
    api_instance.repositories_repo_name_delete(repo_name)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| The name of repository which will be deleted. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_signatures_get**
> list[RepoSignature] repositories_repo_name_signatures_get(repo_name)

Get signature information of a repository

This endpoint aims to retrieve signature information of a repository, the data is from the nested notary instance of Harbor. If the repository does not have any signature information in notary, this API will return an empty list with response code 200, instead of 404 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
repo_name = 'repo_name_example' # str | repository name.

try: 
    # Get signature information of a repository
    api_response = api_instance.repositories_repo_name_signatures_get(repo_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_signatures_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| repository name. | 

### Return type

[**list[RepoSignature]**](RepoSignature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_tags_get**
> list[DetailedTag] repositories_repo_name_tags_get(repo_name)

Get tags of a relevant repository.

This endpoint aims to retrieve tags from a relevant repository. If deployed with Notary, the signature property of response represents whether the image is singed or not. If the property is null, the image is unsigned. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
repo_name = 'repo_name_example' # str | Relevant repository name.

try: 
    # Get tags of a relevant repository.
    api_response = api_instance.repositories_repo_name_tags_get(repo_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Relevant repository name. | 

### Return type

[**list[DetailedTag]**](DetailedTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_tags_tag_delete**
> repositories_repo_name_tags_tag_delete(repo_name, tag)

Delete a tag in a repository.

This endpoint let user delete tags with repo name and tag. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
repo_name = 'repo_name_example' # str | The name of repository which will be deleted.
tag = 'tag_example' # str | Tag of a repository.

try: 
    # Delete a tag in a repository.
    api_instance.repositories_repo_name_tags_tag_delete(repo_name, tag)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_tags_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| The name of repository which will be deleted. | 
 **tag** | **str**| Tag of a repository. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_tags_tag_get**
> DetailedTag repositories_repo_name_tags_tag_get(repo_name, tag)

Get the tag of the repository.

This endpoint aims to retrieve the tag of the repository. If deployed with Notary, the signature property of response represents whether the image is singed or not. If the property is null, the image is unsigned. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
repo_name = 'repo_name_example' # str | Relevant repository name.
tag = 'tag_example' # str | Tag of the repository.

try: 
    # Get the tag of the repository.
    api_response = api_instance.repositories_repo_name_tags_tag_get(repo_name, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_tags_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Relevant repository name. | 
 **tag** | **str**| Tag of the repository. | 

### Return type

[**DetailedTag**](DetailedTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_tags_tag_manifest_get**
> Manifest repositories_repo_name_tags_tag_manifest_get(repo_name, tag, version=version)

Get manifests of a relevant repository.

This endpoint aims to retreive manifests from a relevant repository. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
repo_name = 'repo_name_example' # str | Repository name
tag = 'tag_example' # str | Tag name
version = 'version_example' # str | The version of manifest, valid value are \"v1\" and \"v2\", default is \"v2\" (optional)

try: 
    # Get manifests of a relevant repository.
    api_response = api_instance.repositories_repo_name_tags_tag_manifest_get(repo_name, tag, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_tags_tag_manifest_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **tag** | **str**| Tag name | 
 **version** | **str**| The version of manifest, valid value are \&quot;v1\&quot; and \&quot;v2\&quot;, default is \&quot;v2\&quot; | [optional] 

### Return type

[**Manifest**](Manifest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_tags_tag_scan_post**
> repositories_repo_name_tags_tag_scan_post(repo_name, tag)

Scan the image.

Trigger jobservice to call Clair API to scan the image identified by the repo_name and tag.  Only project admins have permission to scan images under the project. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
repo_name = 'repo_name_example' # str | Repository name
tag = 'tag_example' # str | Tag name

try: 
    # Scan the image.
    api_instance.repositories_repo_name_tags_tag_scan_post(repo_name, tag)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_tags_tag_scan_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **tag** | **str**| Tag name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_repo_name_tags_tag_vulnerability_details_get**
> list[DefinitionsVulnerabilityItem] repositories_repo_name_tags_tag_vulnerability_details_get(repo_name, tag)

Get vulnerability details of the image.

Call Clair API to get the vulnerability based on the previous successful scan. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
repo_name = 'repo_name_example' # str | Repository name
tag = 'tag_example' # str | Tag name

try: 
    # Get vulnerability details of the image.
    api_response = api_instance.repositories_repo_name_tags_tag_vulnerability_details_get(repo_name, tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_repo_name_tags_tag_vulnerability_details_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**| Repository name | 
 **tag** | **str**| Tag name | 

### Return type

[**list[DefinitionsVulnerabilityItem]**](DefinitionsVulnerabilityItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repositories_top_get**
> list[Repository] repositories_top_get(count=count)

Get public repositories which are accessed most.

This endpoint aims to let users see the most popular public repositories 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
count = 56 # int | The number of the requested public repositories, default is 10 if not provided. (optional)

try: 
    # Get public repositories which are accessed most.
    api_response = api_instance.repositories_top_get(count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->repositories_top_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| The number of the requested public repositories, default is 10 if not provided. | [optional] 

### Return type

[**list[Repository]**](Repository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_get**
> list[Search] search_get(q)

Search for projects and repositories

The Search endpoint returns information about the projects and repositories offered at public status or related to the current logged in user. The response includes the project and repository list in a proper display order. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
q = 'q_example' # str | Search parameter for project and repository name.

try: 
    # Search for projects and repositories
    api_response = api_instance.search_get(q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Search parameter for project and repository name. | 

### Return type

[**list[Search]**](Search.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **statistics_get**
> StatisticMap statistics_get()

Get projects number and repositories number relevant to the user

This endpoint is aimed to statistic all of the projects number and repositories number relevant to the logined user, also the public projects number and repositories number. If the user is admin, he can also get total projects number and total repositories number. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()

try: 
    # Get projects number and repositories number relevant to the user
    api_response = api_instance.statistics_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->statistics_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatisticMap**](StatisticMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminfo_get**
> object systeminfo_get()

Get general system info

This API is for retrieving general system info, this can be called by anonymous request. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()

try: 
    # Get general system info
    api_response = api_instance.systeminfo_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->systeminfo_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminfo_getcert_get**
> systeminfo_getcert_get()

Get default root certificate under OVA deployment.

This endpoint is for downloading a default root certificate that only provides for admin user under OVA deployment. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()

try: 
    # Get default root certificate under OVA deployment.
    api_instance.systeminfo_getcert_get()
except ApiException as e:
    print("Exception when calling ProductsApi->systeminfo_getcert_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systeminfo_volumes_get**
> object systeminfo_volumes_get()

Get system volume info (total/free size).

This endpoint is for retrieving system volume info that only provides for admin user. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()

try: 
    # Get system volume info (total/free size).
    api_response = api_instance.systeminfo_volumes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->systeminfo_volumes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **targets_get**
> list[RepTarget] targets_get(name=name)

List filters targets by name.

This endpoint let user list filters targets by name, if name is nil, list returns all targets. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
name = 'name_example' # str | The replication's target name. (optional)

try: 
    # List filters targets by name.
    api_response = api_instance.targets_get(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->targets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The replication&#39;s target name. | [optional] 

### Return type

[**list[RepTarget]**](RepTarget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **targets_id_delete**
> targets_id_delete(id)

Delete specific replication's target.

This endpoint is for to delete specific replication's target. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
id = 789 # int | The replication's target ID.

try: 
    # Delete specific replication's target.
    api_instance.targets_id_delete(id)
except ApiException as e:
    print("Exception when calling ProductsApi->targets_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The replication&#39;s target ID. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **targets_id_get**
> RepTarget targets_id_get(id)

Get replication's target.

This endpoint is for get specific replication's target.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
id = 789 # int | The replication's target ID.

try: 
    # Get replication's target.
    api_response = api_instance.targets_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->targets_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The replication&#39;s target ID. | 

### Return type

[**RepTarget**](RepTarget.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **targets_id_ping_post**
> targets_id_ping_post(id)

Ping target.

This endpoint is for ping target. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
id = 789 # int | The replication's target ID.

try: 
    # Ping target.
    api_instance.targets_id_ping_post(id)
except ApiException as e:
    print("Exception when calling ProductsApi->targets_id_ping_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The replication&#39;s target ID. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **targets_id_policies_get**
> list[RepPolicy] targets_id_policies_get(id)

List the target relevant policies.

This endpoint list policies filter with specific replication's target ID. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
id = 789 # int | The replication's target ID.

try: 
    # List the target relevant policies.
    api_response = api_instance.targets_id_policies_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->targets_id_policies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The replication&#39;s target ID. | 

### Return type

[**list[RepPolicy]**](RepPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **targets_id_put**
> targets_id_put(id, repo_target)

Update replication's target.

This endpoint is for update specific replication's target. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
id = 789 # int | The replication's target ID.
repo_target = swagger_client.PutTarget() # PutTarget | Updates of replication's target.

try: 
    # Update replication's target.
    api_instance.targets_id_put(id, repo_target)
except ApiException as e:
    print("Exception when calling ProductsApi->targets_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The replication&#39;s target ID. | 
 **repo_target** | [**PutTarget**](PutTarget.md)| Updates of replication&#39;s target. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **targets_ping_post**
> targets_ping_post(target)

Ping validates target.

This endpoint is for ping validates whether the target is reachable and whether the credential is valid. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
target = swagger_client.PingTarget() # PingTarget | The target object.

try: 
    # Ping validates target.
    api_instance.targets_ping_post(target)
except ApiException as e:
    print("Exception when calling ProductsApi->targets_ping_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | [**PingTarget**](PingTarget.md)| The target object. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **targets_post**
> targets_post(reptarget)

Create a new replication target.

This endpoint is for user to create a new replication target. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
reptarget = swagger_client.RepTargetPost() # RepTargetPost | New created replication target.

try: 
    # Create a new replication target.
    api_instance.targets_post(reptarget)
except ApiException as e:
    print("Exception when calling ProductsApi->targets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reptarget** | [**RepTargetPost**](RepTargetPost.md)| New created replication target. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_current_get**
> User users_current_get()

Get current user info.

This endpoint is to get the current user infomation. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()

try: 
    # Get current user info.
    api_response = api_instance.users_current_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->users_current_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get**
> list[User] users_get(username=username, email=email, page=page, page_size=page_size)

Get registered users of Harbor.

This endpoint is for user to search registered users, support for filtering results with username.Notice, by now this operation is only for administrator. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
username = 'username_example' # str | Username for filtering results. (optional)
email = 'email_example' # str | Email for filtering results. (optional)
page = 56 # int | The page nubmer, default is 1. (optional)
page_size = 56 # int | The size of per page. (optional)

try: 
    # Get registered users of Harbor.
    api_response = api_instance.users_get(username=username, email=email, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username for filtering results. | [optional] 
 **email** | **str**| Email for filtering results. | [optional] 
 **page** | **int**| The page nubmer, default is 1. | [optional] 
 **page_size** | **int**| The size of per page. | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_post**
> users_post(user)

Creates a new user account.

This endpoint is to create a user if the user does not already exist. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
user = swagger_client.User() # User | New created user.

try: 
    # Creates a new user account.
    api_instance.users_post(user)
except ApiException as e:
    print("Exception when calling ProductsApi->users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**User**](User.md)| New created user. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_delete**
> users_user_id_delete(user_id)

Mark a registered user as be removed.

This endpoint let administrator of Harbor mark a registered user as be removed.It actually won't be deleted from DB. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
user_id = 56 # int | User ID for marking as to be removed.

try: 
    # Mark a registered user as be removed.
    api_instance.users_user_id_delete(user_id)
except ApiException as e:
    print("Exception when calling ProductsApi->users_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID for marking as to be removed. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_get**
> users_user_id_get(user_id)

Get a user's profile.

Get user's profile with user id. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
user_id = 56 # int | Registered user ID

try: 
    # Get a user's profile.
    api_instance.users_user_id_get(user_id)
except ApiException as e:
    print("Exception when calling ProductsApi->users_user_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Registered user ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_password_put**
> users_user_id_password_put(user_id, password)

Change the password on a user that already exists.

This endpoint is for user to update password. Users with the admin role can change any user's password. Guest users can change only their own password. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
user_id = 56 # int | Registered user ID.
password = swagger_client.Password() # Password | Password to be updated.

try: 
    # Change the password on a user that already exists.
    api_instance.users_user_id_password_put(user_id, password)
except ApiException as e:
    print("Exception when calling ProductsApi->users_user_id_password_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Registered user ID. | 
 **password** | [**Password**](Password.md)| Password to be updated. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_put**
> users_user_id_put(user_id, profile)

Update a registered user to change his profile.

This endpoint let a registered user change his profile. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
user_id = 56 # int | Registered user ID
profile = swagger_client.UserProfile() # UserProfile | Only email, realname and comment can be modified.

try: 
    # Update a registered user to change his profile.
    api_instance.users_user_id_put(user_id, profile)
except ApiException as e:
    print("Exception when calling ProductsApi->users_user_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Registered user ID | 
 **profile** | [**UserProfile**](UserProfile.md)| Only email, realname and comment can be modified. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_id_sysadmin_put**
> users_user_id_sysadmin_put(user_id, has_admin_role)

Update a registered user to change to be an administrator of Harbor.

This endpoint let a registered user change to be an administrator of Harbor. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
user_id = 56 # int | Registered user ID
has_admin_role = swagger_client.HasAdminRole() # HasAdminRole | Toggle a user to admin or not.

try: 
    # Update a registered user to change to be an administrator of Harbor.
    api_instance.users_user_id_sysadmin_put(user_id, has_admin_role)
except ApiException as e:
    print("Exception when calling ProductsApi->users_user_id_sysadmin_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Registered user ID | 
 **has_admin_role** | [**HasAdminRole**](HasAdminRole.md)| Toggle a user to admin or not. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

