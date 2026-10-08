local KIND = {kid="kidbox", ai="aibox", warn="warnbox", ex="exbox"}
local DOCX = {kid="BoxKid", ai="BoxAI", warn="BoxWarn", ex="BoxEx"}
local in_appendix = false
local appendix_letter = 0

function Div(el)
  if el.classes:includes("box") then
    local kind = el.attributes.kind or "kid"
    local title = el.attributes.title or ""
    if FORMAT:match("latex") then
      local blocks = {pandoc.RawBlock("latex", "\\begin{" .. KIND[kind] .. "}{" .. title .. "}")}
      for _, b in ipairs(el.content) do table.insert(blocks, b) end
      table.insert(blocks, pandoc.RawBlock("latex", "\\end{" .. KIND[kind] .. "}"))
      return blocks
    elseif FORMAT:match("docx") then
      local out = {}
      table.insert(out, pandoc.Div({pandoc.Para({pandoc.Strong(pandoc.Str(title))})}, {["custom-style"]=DOCX[kind] .. "Title"}))
      local body = {}
      for _, b in ipairs(el.content) do
        if b.t == "CodeBlock" then
          if #body > 0 then table.insert(out, pandoc.Div(body, {["custom-style"]=DOCX[kind]})); body = {} end
          table.insert(out, b)
        else table.insert(body, b) end
      end
      if #body > 0 then table.insert(out, pandoc.Div(body, {["custom-style"]=DOCX[kind]})) end
      table.insert(out, pandoc.Para({}))
      return out
    end
  elseif el.classes:includes("part") then
    local t = el.attributes.title
    if FORMAT:match("latex") then
      return pandoc.RawBlock("latex", "\\mypart{" .. t .. "}")
    else
      return {pandoc.RawBlock("openxml", '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'),
              pandoc.Div({pandoc.Para({pandoc.Str(t)})}, {["custom-style"]="PartTitle"})}
      -- không thêm ngắt trang ở cuối: chương (#) ngay sau đã tự ngắt trang
    end
  elseif el.classes:includes("appendix") then
    in_appendix = true
    if FORMAT:match("latex") then return pandoc.RawBlock("latex", "\\appendix") end
    return {}
  end
end

function Header(el)
  if FORMAT:match("docx") and el.level == 1 then
    if in_appendix then
      appendix_letter = appendix_letter + 1
      el.classes:insert("unnumbered")
      local L = string.char(64 + appendix_letter)
      table.insert(el.content, 1, pandoc.Str("Phụ lục " .. L .. ". "))
      return {pandoc.RawBlock("openxml", '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'), el}
    end
    return {pandoc.RawBlock("openxml", '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'), el}
  end
end

-- run Div first then Header so in_appendix is set in document order
return {{Pandoc = function(doc)
  local blocks = {}
  for _, b in ipairs(doc.blocks) do
    local r
    if b.t == "Div" then r = Div(b) elseif b.t == "Header" then r = Header(b) end
    if r == nil then table.insert(blocks, b)
    elseif r.t then table.insert(blocks, r)
    else for _, x in ipairs(r) do table.insert(blocks, x) end end
  end
  doc.blocks = blocks
  return doc
end}}
