# ae-to-json

[![experimental](http://badges.github.io/stability-badges/dist/experimental.svg)](http://github.com/badges/stability-badges)

The purpose of this module is to create After Effects JSX/JS Script cript to:
- Export After Effects files as JSON like Objects
- Standardize After Effects to JSON Exporters
- Create a platform on which renderers can be built on top of
- Have proper unit tests to catch breaking changes in After Effects

Documentation on Adobe's After Effects scripting guide can be found here:
- [After Effects Scripting Guide](http://download.macromedia.com/pub/developer/aftereffects/scripting/After-Effects-CS6-Scripting-Guide.pdf) _(appendix of API documentation starts on Page #12)_
- [Javascript Tools Guide](https://www.adobe.com/content/dam/Adobe/en/devnet/scripting/pdfs/javascript_tools_guide.pdf)

## Usage

[![NPM](https://nodei.co/npm/ae-to-json.png)](https://www.npmjs.com/package/ae-to-json)

There are a few ways that you can consume this module. They are documented below:

- [Usage with the `after-effects` module](#usage-with-the-after-effects-module)
- [Usage in After Effects' Scripting tools](#usage-in-after-effects-scripting-tools)
- [Build and use in your own JSX Scripts](#build-and-use-in-your-own-jsx-scripts)

### Usage with the `after-effects` module

The [`after-effects`](https://www.npmjs.com/package/after-effects) allows you to run "functions" in After effects. Pass it one function it will return you the value in Node. No need to use the After Effects Scripting tools. To use with [`after-effects`](https://www.npmjs.com/package/after-effects):

Install `after-effects`:
```bash
$ npm i ae-to-json after-effects --save
```

In Javascript:
```javascript
var aeToJSON = require('ae-to-json/after-effects');
var ae = require('after-effects');

ae.execute(aeToJSON)
.then(function(json) {
  // do something with the json outout
})
.catch(function(e) {
  throw e;
});
```

### Usage in After Effects' Scripting tools

Copy the contents of `dist/index.js`. The dist build will bring in es-5 shims and a JSON shim.

In After Effects go to:

- File
- Scripts
- Open Script Editor
- Paste contents into Script Editor

You should now be able to do something like:
```javascript
JSON.stringify(aeToJSON(), null, '  ');
```

### Build and use in your own JSX Scripts

Since After Effects currently uses a Ecma Script 3 engine you will need to shim in Ecma Script 5. Also you should shim in JSON also.

Install:
```bash
$ npm i ae-to-json es5-shim JSON2 --save
```

Javascript:
```javascript
// shim in es5 functionality
require('es5-shim');

// you might want to make JSON be a global
JSON = require('JSON2');

var aeToJSON = require('ae-to-json');

// do something with the aeToJSON function
```

After this you'll most likely want to browserify the Javascript file defined above.

```bash
$ browserify index.js -o bundle.js
```



## High Level Exported Format

Here's an example on an high level what will be exported from After Effects. For a more detailed example of an export check out:
[https://raw.githubusercontent.com/Jam3/ae-to-json/master/example/example.json](https://raw.githubusercontent.com/Jam3/ae-to-json/master/example/example.json)

These files can be very large since we attempt to export everything but at least this small bit of documentation will help you get started traversing the exports:
```javascript
{ 
  // meta data for the project
  project: {

    // items which are used in the Project panel
    // this includes: 
    //  Compositions, 
    //  Footage (images, videos, solids, etc.),
    //  Solids,
    //  etc.
    items: [
      // Composition Type
      {
        typeName: 'Composition',
        // these are the Compositions layers
        layers: [
          {
            // this includes all properties for this layer
            // properties are things like:
            //  Transform, (position, scale, rotation, anchor, etc.)
            //  Material Options,
            //  Effects,
            //  etc.
            properties: {

              // this is what the transform property would look like
              Transform: {

                // Transform's have their own properties
                // This is what X Position on a high level would look like
                "X Position": {

                  // if a property is animatable it will contain keyframes
                  // keyframes will be a two dimension array where each element
                  // on the second dimension is a key frame
                  "keyframes": [
                    // each key frame has a time (in seconds) which is at [0]
                    // a value which is at [1] (values can be scalar values 
                    // or arrays represented by arrays)
                    // 
                    // And an optional ease value. Generally you'd need more
                    // than one keyframe to have ease values.
                    // 
                    // It should be noted if no keyframes were added in After 
                    // Effects for ease of use one keyframe will be output with
                    // the value at time 0
                    [ time, value, ease ]
                  ]
                }
              }
            }
          }
        ]
      },
      {
        typeName: 'Footage'
      },
      {
        typeName: 'Folder',
        items: [
          // this items folder would contain
          // Compositions, Footage, Solids, etc.
        ]
      }
    ]
  }
}
```

## Export Example

You can view an export example at (be forewarned these files are huge):

[https://raw.githubusercontent.com/Jam3/ae-to-json/master/example/example.json](https://raw.githubusercontent.com/Jam3/ae-to-json/master/example/example.json)

## Testing

To run tests there are two scenarios. Run a test just once or watch the `src/`and `test/` folders and run tests. Below are the commands to run tests:

To run test once:
```bash
$ npm test
```

To watch and run (better for development):
```bash
$ npm start
```

When run unit tests are run on the JSON out along with a `testOutput.json` file is exported to the root director of this repo.

## License

MIT, see [LICENSE.md](http://github.com/jam3/ae-to-json/blob/master/LICENSE.md) for details.
