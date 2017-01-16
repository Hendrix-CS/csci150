{-# LANGUAGE OverloadedStrings #-}

import           Hakyll
import           Hakyll.Web.Course

import           Control.Monad     ((>=>))
import           Data.Monoid       ((<>))

main = do
  hakyll $ do

    standardRules staticContent
    createIndex sections
  where
    staticContent = ["images/*", "docs/*", "static/*", "data/*", "labs/*", "homework/*"]
    sections = ["overview", "syllabus", "quizhw", "labs", "projects", "exams", "grading"]
