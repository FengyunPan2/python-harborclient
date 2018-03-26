# Project

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Project ID | [optional] 
**owner_id** | **int** | The owner ID of the project always means the creator of the project. | [optional] 
**name** | **str** | The name of the project. | [optional] 
**creation_time** | **str** | The creation time of the project. | [optional] 
**update_time** | **str** | The update time of the project. | [optional] 
**deleted** | **int** | A deletion mark of the project (1 means it&#39;s deleted, 0 is not) | [optional] 
**owner_name** | **str** | The owner name of the project. | [optional] 
**public** | **int** | The public status of the project. | [optional] 
**togglable** | **bool** | Correspond to the UI about whether the project&#39;s publicity is  updatable (for UI) | [optional] 
**current_user_role_id** | **int** | The role ID of the current user who triggered the API (for UI) | [optional] 
**repo_count** | **int** | The number of the repositories under this project. | [optional] 
**enable_content_trust** | **bool** | Whether content trust is enabled or not. If it is enabled, user cann&#39;t pull unsigned images from this project. | [optional] 
**prevent_vulnerable_images_from_running** | **bool** | Whether prevent the vulnerable images from running. | [optional] 
**prevent_vulnerable_images_from_running_severity** | **str** | If the vulnerability is high than severity defined here, the images cann&#39;t be pulled. | [optional] 
**automatically_scan_images_on_push** | **bool** | Whether scan images automatically when pushing. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


