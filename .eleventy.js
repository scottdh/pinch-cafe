module.exports = function (eleventyConfig) {
  // Set directories to pass through to the dist folder
  eleventyConfig.addPassthroughCopy("./src/fonts/");

  eleventyConfig.addWatchTarget("./src/sass/");

  return {
    dir: {
      input: "src",
      output: "public",
    },
  };
};
