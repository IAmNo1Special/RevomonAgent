from revomonauto.controllers.revo_controller import RevoAppController


class _App_Config:
    def __init__(self):
        self.REVO_APP_CONTROLLER = None
        self.APP_NAME: str = "revo_agent"
        self.USER_ID: str = "user1"
        self.SESSION_ID: str = "session1"
        self.connect_revoappcontroller()

    def connect_revoappcontroller(self) -> None:
        """
        Connect to the RevoAppController, creating it only if it doesn't exist.

        Returns:
            None
        """
        if not self.REVO_APP_CONTROLLER:
            self.REVO_APP_CONTROLLER = RevoAppController()
        return None


app_config = _App_Config()
