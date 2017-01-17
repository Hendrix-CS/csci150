{-# LANGUAGE OverloadedStrings #-}

import           Hakyll
import           Hakyll.Web.Course

import           Control.Monad     ((>=>))
import           Data.Monoid       ((<>))

main = do
  hakyll $ do

    standardRules staticContent
    createIndex sections

    match "labs/*" $ do
      route $ setExtension "html"
      compile labCompiler

  where
    staticContent = ["images/*", "docs/*", "static/*", "data/*", "homework/*"]
    sections = ["overview", "syllabus", "quizhw", "labs", "projects", "exams", "grading"]

labCompiler :: Compiler (Item String)
labCompiler =
    pandocCompiler
    >>= loadAndApplyTemplate "templates/lab.html" defaultContext
    >>= relativizeUrls
