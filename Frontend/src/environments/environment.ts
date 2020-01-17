// The file contents for the current environment will overwrite these during build.
// The build system defaults to the dev environment which uses `environment.ts`, but if you do
// `ng build --env=prod` then `environment.prod.ts` will be used instead.
// The list of which env maps to which file can be found in `.angular-cli.json`.

export const environment = {
  production: false,
  firebase: {
    apiKey: 'AIzaSyA60pxujJvEyhN6SkANmkhSqUMLMaJEgDI',
    authDomain: 'questionsandanswersdatabase.firebaseapp.com',
    databaseURL: 'https://questionsandanswersdatabase.firebaseio.com',
    projectId: 'questionsandanswersdatabase',
    storageBucket: 'questionsandanswersdatabase.appspot.com',
    messagingSenderId: '610071156368',
    appId: '1:610071156368:web:73bb8022a2c8dedc'
  }
};
