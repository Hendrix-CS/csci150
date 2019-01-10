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

    match "projects/*" $ do
      route $ setExtension "html"
      compile labCompiler

  where
    staticContent = ["images/*", "docs/*", "static/*", "data/*", "homework/*"]
    sections = ["inclass", "quizhw", "labs", "projects", "exams", "syllabus"]

labCompiler :: Compiler (Item String)
labCompiler =
    getResourceBody
    >>= loadAndApplyTemplate "templates/lab.html" defaultContext
    >>= relativizeUrls
