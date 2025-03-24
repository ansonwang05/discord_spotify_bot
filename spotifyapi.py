import spotapi
import spotify_api_key_gen

api_key = spotify_api_key_gen.get_token()
email = "spotifyapi123@gmail.com"
password = "spotifyapi123"

cfg = spotapi.Config(
    solver = spotapi.solver_clients.Capsolver(api_key),
    logger = spotapi.NoopLogger(),
)

instance = spotapi.Login(cfg, password, email)
instance.login()

instance.save(spotapi.MongoSaver())
print("Logged in Successfully!")
