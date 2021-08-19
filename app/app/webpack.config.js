const path = require('path');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const { WebpackManifestPlugin } = require('webpack-manifest-plugin');
const options = {};
const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = (env) => {

    let output_string = '[name].[contenthash].js'
    if(env.development) {
        console.log(env.development)
        output_string = '[name].js'
    }

    return {
        mode: 'development',
            entry: {
            'home' : './src/home.js',
            'users' : './src/users.js',
        },
        resolve: {
            alias: {
                'vue$': 'vue/dist/vue.esm.js'
            },
            extensions: ['*', '.js', '.vue', '.json']
        },
        output: {
            filename: output_string,
            path: path.resolve(__dirname, 'static/js/app'),
        },
        plugins: [
            new CleanWebpackPlugin(),
            new WebpackManifestPlugin(options),
            new VueLoaderPlugin()
        ],
            module: {
        rules: [
            {
                test: /\.m?js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader",
                    options: {
                        presets: ['@babel/preset-env']
                    }
                }
            },
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            }
        ]
    }
    }
};