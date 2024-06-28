def model(dbt, session):
    from snowflake.snowpark.session import Session

    from snowflake.snowpark.types import Variant

    # Must be either table or incremental (view is not currently supported)
    dbt.config(materialized = "table")
    
    session.add_import("/Users/mitaylor/Documents/GitHub/AA Cleaned Repos/Import_Packages_Demo/dist/hello_world_pkg-1.0-py3-none-any.whl")
    session.add_import("/Users/mitaylor/Documents/GitHub/AA Cleaned Repos/Import_Packages_Demo/wheel_loader.py")
    
    import wheel_loader
    wheel_loader.load('hello_world_pkg-1.0-py3-none-any.whl')
    import hello_world_pkg 
    df_name = hello_world_pkg.hello_world.test_hello_world_pkg()
    # def py_whl_pkg_sproc(session: Session) -> Variant:
    #     import wheel_loader
    #     wheel_loader.load('hello_world_pkg-1.0-py3-none-any.whl')
    #     import hello_world_pkg 
    #     return(hello_world_pkg.hello_world.test_hello_world_pkg())

    #     # Register sproc
    #     py_whl_pkg_sproc = session.sproc.register(
    #                                 func=py_whl_pkg_sproc, 
    #                                 name='PY_WHL_PKG_SPROC', 
    #                                 is_permanent=True, 
    #                                 replace=True,
    #                                 stage_location='@PACKAGE_STAGE', 
    #                                 packages=['snowflake-snowpark-python'],
    #                                 imports=["@PACKAGE_STAGE/wheel_loader.py",
    #                                         "@PACKAGE_STAGE/hello_world_pkg-1.0-py3-none-any.whl"])
    # # Call sproc
    # py_whl_pkg_sproc()

    # DataFrame representing an upstream model
    df = dbt.ref("my_first_dbt_model")
 
    return df